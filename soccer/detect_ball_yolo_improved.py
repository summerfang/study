import os
import cv2
from ultralytics import YOLO

def detect_and_mark_ball_yolo(image_path, output_path, model_path='yolov8n.pt', conf=0.15):
    # Read image at original resolution
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return
    height, width = image.shape[:2]

    # Load YOLO model
    model = YOLO(model_path)
    # Set imgsz to the max dimension (width or height, whichever is larger and divisible by 32)
    imgsz = max(width, height)
    # Make sure imgsz is divisible by 32 (YOLO requirement)
    imgsz = (imgsz // 32) * 32

    results = model(image, conf=conf, imgsz=imgsz)

    ball_found = False
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            # For COCO models, 'sports ball' is usually class 32
            if hasattr(result, 'names') and result.names[cls].lower() in ['sports ball', 'ball']:
                x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                ball_found = True

    if ball_found:
        cv2.imwrite(output_path, image)
        print(f"Ball marked and saved to {output_path}")
    else:
        print(f"No ball detected in {image_path}")

if __name__ == "__main__":
    photo_dir = "photo"
    detect_and_mark_ball_yolo(os.path.join(photo_dir, "soccer_6s.png"), os.path.join(photo_dir, "p1_ball.png"))
    detect_and_mark_ball_yolo(os.path.join(photo_dir, "soccer_7s.png"), os.path.join(photo_dir, "p2_ball.png"))