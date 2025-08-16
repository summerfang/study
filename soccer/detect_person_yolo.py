import os
from ultralytics import YOLO
import cv2

def detect_and_mark_person_yolo(image_path, output_path, model_path='yolov8n.pt'):
    # Load YOLO model (use yolov8n.pt or another YOLO model)
    model = YOLO(model_path)
    results = model(image_path)

    # Read image
    image = cv2.imread(image_path)
    person_found = False

    # Iterate through detections
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            # For COCO models, class 0 is 'person'
            if hasattr(result, 'names') and result.names[cls].lower() == 'person':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
                person_found = True

    if person_found:
        cv2.imwrite(output_path, image)
        print(f"Person(s) marked and saved to {output_path}")
    else:
        print(f"No person detected in {image_path}")

if __name__ == "__main__":
    photo_dir = "photo"
    detect_and_mark_person_yolo(os.path.join(photo_dir, "p1.png"), os.path.join(photo_dir, "p1_person.png"))
    detect_and_mark_person_yolo(os.path.join(photo_dir, "p2.png"), os.path.join(photo_dir, "p2_person.png"))