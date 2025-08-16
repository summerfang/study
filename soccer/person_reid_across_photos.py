import os
import cv2
from ultralytics import YOLO
import torch
from torchreid.utils import FeatureExtractor

def detect_persons_yolo(image_path, model_path='yolov8n.pt'):
    model = YOLO(model_path)
    results = model(image_path)
    image = cv2.imread(image_path)
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
    features = extractor(crops)
    return features

def match_persons(features1, features2, threshold=0.5):
    # Compute cosine similarity and assign IDs
    from sklearn.metrics.pairwise import cosine_similarity
    sim_matrix = cosine_similarity(features1, features2)
    matches = []
    for i, row in enumerate(sim_matrix):
        j = row.argmax()
        if row[j] > threshold:
            matches.append((i, j))
    return matches

if __name__ == "__main__":
    photo_dir = "photo"
    img1_path = os.path.join(photo_dir, "p3.png")
    img2_path = os.path.join(photo_dir, "p4.png")

    # Step 1: Detect persons
    img1, boxes1 = detect_persons_yolo(img1_path)
    img2, boxes2 = detect_persons_yolo(img2_path)

    # Step 2: Extract features using deep-person-reid
    extractor = FeatureExtractor(
        model_name='osnet_x1_0',
        model_path='osnet_x1_0_imagenet.pth',  # Download from deep-person-reid repo
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )
    features1 = extract_features(img1, boxes1, extractor)
    features2 = extract_features(img2, boxes2, extractor)

    # Step 3: Match persons across images
    matches = match_persons(features1, features2)

    # Step 4: Draw boxes and IDs
    for idx, (x1, y1, x2, y2) in enumerate(boxes1):
        cv2.rectangle(img1, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img1, f"ID:{idx}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
    for idx, (x1, y1, x2, y2) in enumerate(boxes2):
        matched = [m[0] for m in matches if m[1] == idx]
        id_text = f"ID:{matched[0]}" if matched else f"ID:?"
        cv2.rectangle(img2, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img2, id_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    cv2.imwrite(os.path.join(photo_dir, "p3_person_reid.png"), img1)
    cv2.imwrite(os.path.join(photo_dir, "p4_person_reid.png"), img2)
    print("Person ReID results saved.")
