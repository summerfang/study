import os
import cv2
from ultralytics import YOLO
import torch
from torchreid.utils import FeatureExtractor
from sklearn.metrics.pairwise import cosine_similarity

PHOTO_DIR = "photo"
DOWNLOAD_DIR = "download"
VIDEO_FILE = os.path.join(DOWNLOAD_DIR, "soccer.mkv")
BALL_MODEL_PATH = "yolov8n.pt"
PERSON_MODEL_PATH = "yolov8n.pt"
REID_MODEL_NAME = "osnet_x1_0"
REID_MODEL_PATH = "osnet_x1_0_imagenet.pth"  # Download from deep-person-reid repo

def extract_frames(video_path, output_dir, num_frames=10):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    for i in range(1, num_frames + 1):
        frame_num = int(fps * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if ret:
            out_path = os.path.join(output_dir, f"p{i}.png")
            cv2.imwrite(out_path, frame)
            print(f"Saved {out_path}")
        else:
            print(f"Failed to extract frame {i}")
    cap.release()

def detect_ball(image_path, output_path, model_path=BALL_MODEL_PATH, conf=0.15):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return
    height, width = image.shape[:2]
    model = YOLO(model_path)
    imgsz = (max(width, height) // 32) * 32
    results = model(image, conf=conf, imgsz=imgsz)
    ball_found = False
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if hasattr(result, 'names') and result.names[cls].lower() in ['sports ball', 'ball']:
                x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                ball_found = True
    cv2.imwrite(output_path, image)
    print(f"Ball detection saved to {output_path}")

def detect_persons(image_path, model_path=PERSON_MODEL_PATH, conf=0.3):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return image, []
    height, width = image.shape[:2]
    model = YOLO(model_path)
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

def extract_features(image, boxes, extractor):
    crops = [image[y1:y2, x1:x2] for (x1, y1, x2, y2) in boxes]
    if not crops:
        return []
    features = extractor(crops)
    return features

def reid_and_draw(images, all_boxes, all_features):
    # Assign IDs based on feature similarity across frames
    ids_per_frame = []
    next_id = 0
    id_features = []

    for frame_idx, features in enumerate(all_features):
        frame_ids = []
        if frame_idx == 0:
            # First frame: assign new IDs
            for i in range(len(features)):
                frame_ids.append(next_id)
                id_features.append(features[i])
                next_id += 1
        else:
            # Match to previous IDs
            sim_matrix = cosine_similarity(features, id_features)
            for i, row in enumerate(sim_matrix):
                j = row.argmax()
                if row[j] > 0.5:
                    frame_ids.append(j)
                else:
                    frame_ids.append(next_id)
                    id_features.append(features[i])
                    next_id += 1
        ids_per_frame.append(frame_ids)

    # Draw boxes and IDs
    for idx, (image, boxes, ids) in enumerate(zip(images, all_boxes, ids_per_frame)):
        for box, pid in zip(boxes, ids):
            x1, y1, x2, y2 = box
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image, f"ID:{pid}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
        out_path = os.path.join(PHOTO_DIR, f"p{idx+1}_person.png")
        cv2.imwrite(out_path, image)
        print(f"Person ReID saved to {out_path}")

if __name__ == "__main__":
    os.makedirs(PHOTO_DIR, exist_ok=True)

    # Step 1: Extract frames
    extract_frames(VIDEO_FILE, PHOTO_DIR, num_frames=10)

    # Step 2: Ball detection
    for i in range(1, 11):
        img_path = os.path.join(PHOTO_DIR, f"p{i}.png")
        out_path = os.path.join(PHOTO_DIR, f"p{i}_ball.png")
        detect_ball(img_path, out_path)

    # Step 3: Person detection and ReID
    extractor = FeatureExtractor(
        model_name=REID_MODEL_NAME,
        model_path=REID_MODEL_PATH,
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )
    images = []
    all_boxes = []
    all_features = []
    for i in range(1, 11):
        img_path = os.path.join(PHOTO_DIR, f"p{i}.png")
        image, boxes = detect_persons(img_path)
        features = extract_features(image, boxes, extractor)
        images.append(image)
        all_boxes.append(boxes)
        all_features.append(features)
    reid_and_draw(images, all_boxes, all_features)