import os
import sys
import cv2
import numpy as np
from ultralytics import YOLO
import torch
from torchreid.utils import FeatureExtractor
from sklearn.metrics.pairwise import cosine_similarity
import argparse

PHOTO_DIR = "photo"
VIDEO_FILE = os.path.join("download", "soccer.mkv")
PERSON_MODEL_PATH = "yolov8n.pt"
REID_MODEL_NAME = "osnet_x1_0"
REID_MODEL_PATH = "osnet_x1_0_imagenet.pth"

def extract_frame(video_path, output_path, time_sec):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = int(fps * time_sec)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
    cap.release()

def detect_persons(image_path, model_path=PERSON_MODEL_PATH, conf=0.3):
    image = cv2.imread(image_path)
    model = YOLO(model_path)
    height, width = image.shape[:2]
    imgsz = (max(width, height) // 32) * 32
    results = model(image, conf=conf, imgsz=imgsz)
    boxes = []
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if hasattr(result, 'names') and result.names[cls].lower() == 'person':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))
    return image, boxes

def detect_ball(image_path, output_path, model_path="yolov8n.pt", conf=0.15):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return None
    height, width = image.shape[:2]
    model = YOLO(model_path)
    imgsz = (max(width, height) // 32) * 32
    results = model(image, conf=conf, imgsz=imgsz)
    ball_box = None
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if hasattr(result, 'names') and result.names[cls].lower() in ['sports ball', 'ball']:
                x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                ball_box = (x1, y1, x2, y2)
    cv2.imwrite(output_path, image)
    return ball_box

def extract_features(image, boxes, extractor):
    crops = [image[y1:y2, x1:x2] for (x1, y1, x2, y2) in boxes]
    if not crops:
        return []
    features = extractor(crops)
    return features

def match_persons(features1, features2, threshold=0.5):
    sim_matrix = cosine_similarity(features1, features2)
    matches = {}
    used = set()
    for i, row in enumerate(sim_matrix):
        j = row.argmax()
        if row[j] > threshold and j not in used:
            matches[j] = i
            used.add(j)
    return matches

def draw_person_boxes(img1, boxes1, img2, boxes2, matches):
    # Draw for img1
    for idx, (x1, y1, x2, y2) in enumerate(boxes1):
        cv2.rectangle(img1, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img1, f"ID:{idx}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
    # Draw for img2
    for idx, (x1, y1, x2, y2) in enumerate(boxes2):
        matched = matches.get(idx, None)
        id_text = f"ID:{matched}" if matched is not None else f"ID:?"
        cv2.rectangle(img2, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img2, id_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

def ball_person_distance(ball_box, person_boxes, ids, top_n=1):
    if not ball_box or not person_boxes:
        return []
    bx = (ball_box[0] + ball_box[2]) // 2
    by = (ball_box[1] + ball_box[3]) // 2
    distances = []
    for box, pid in zip(person_boxes, ids):
        px = (box[0] + box[2]) // 2
        py = (box[1] + box[3]) // 2
        dist = np.sqrt((px - bx) ** 2 + (py - by) ** 2)
        distances.append((dist, pid))
    distances.sort()
    return [f"ID{pid}" for _, pid in distances[:top_n]]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('seconds', nargs='+', type=int, help='Seconds in the video to extract frames')
    parser.add_argument('--closest', type=int, default=1, help='Number of closest persons to the ball (default: 1)')
    args = parser.parse_args()

    os.makedirs(PHOTO_DIR, exist_ok=True)
    seconds = args.seconds
    top_n = args.closest

    extractor = FeatureExtractor(
        model_name=REID_MODEL_NAME,
        model_path=REID_MODEL_PATH,
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )

    images = []
    all_boxes = []
    all_features = []
    ball_boxes = []

    # Step 1: Extract frames and process
    for sec in seconds:
        img_path = os.path.join(PHOTO_DIR, f"p{sec}.png")
        extract_frame(VIDEO_FILE, img_path, sec)
        image, boxes = detect_persons(img_path)
        features = extract_features(image, boxes, extractor)
        ball_img_path = os.path.join(PHOTO_DIR, f"p{sec}_ball.png")
        ball_box = detect_ball(img_path, ball_img_path)
        images.append(image)
        all_boxes.append(boxes)
        all_features.append(features)
        ball_boxes.append(ball_box)

    # Step 2: ReID matching across all frames (pairwise, for N frames)
    # Assign IDs for first frame
    ids_per_frame = []
    ids_per_frame.append(list(range(len(all_boxes[0]))))
    # For subsequent frames, match to previous frame
    for i in range(1, len(all_features)):
        matches = match_persons(all_features[i-1], all_features[i])
        ids = []
        for idx in range(len(all_boxes[i])):
            matched = matches.get(idx, None)
            id_val = ids_per_frame[i-1][matched] if matched is not None else f"?{i}_{idx}"
            ids.append(id_val)
        ids_per_frame.append(ids)

    # Step 3: Draw boxes and output closest N IDs to ball
    for idx, sec in enumerate(seconds):
        img = images[idx]
        boxes = all_boxes[idx]
        ids = ids_per_frame[idx]
        out_path = os.path.join(PHOTO_DIR, f"p{sec}_person.png")
        for box, pid in zip(boxes, ids):
            x1, y1, x2, y2 = box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, f"ID:{pid}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
        cv2.imwrite(out_path, img)
        closest_ids = ball_person_distance(ball_boxes[idx], boxes, ids, top_n=top_n)
        print(f"{sec}s: {closest_ids}")