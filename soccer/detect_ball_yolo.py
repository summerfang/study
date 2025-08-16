import os
from ultralytics import YOLO
import cv2

def detect_and_mark_ball_yolo(image_path, output_path, model_path='yolov5s.pt'):
    # Load YOLO model (replace with your custom model if available)
    model = YOLO(model_path)
    results = model(image_path)

    # Read image
    image = cv2.imread(image_path)
    ball_found = False

    # Iterate through detections
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            # If using a custom model, check for ball class index (e.g., 0)
            # For generic YOLO, you may need to check the label name
            if hasattr(result, 'names') and result.names[cls].lower() == 'sports ball':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                ball_found = True

    if ball_found:
        cv2.imwrite(output_path, image)
        print(f"Ball marked and saved to {output_path}")
    else:
        print(f"No ball detected in {image_path}")

if __name__ == "__main__":
    photo_dir = "photo"
    detect_and_mark_ball_yolo(os.path.join(photo_dir, "p1.png"), os.path.join(photo_dir, "p1_ball.png"))
    detect_and_mark_ball_yolo(os.path.join(photo_dir, "p2.png"), os.path.join(photo_dir, "p2_ball.png"))