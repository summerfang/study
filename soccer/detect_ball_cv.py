import cv2
import numpy as np
import os

def detect_and_mark_ball(image_path, output_path):
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load {image_path}")
        return

    # Convert to HSV for color detection (assuming ball is white)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define range for white color (adjust as needed)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ball_found = False
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Filter by size (adjust min/max as needed)
        if 10 < w < 100 and 10 < h < 100:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            ball_found = True
            break

    if ball_found:
        cv2.imwrite(output_path, image)
        print(f"Ball marked and saved to {output_path}")
    else:
        print(f"No ball detected in {image_path}")

if __name__ == "__main__":
    photo_dir = "photo"
    detect_and_mark_ball(os.path.join(photo_dir, "p1.png"), os.path.join(photo_dir, "p1_ball.png"))
    detect_and_mark_ball(os.path.join(photo_dir, "p2.png"), os.path.join(photo_dir, "p2_ball.png"))