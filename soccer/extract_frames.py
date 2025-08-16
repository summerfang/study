import cv2

def save_frame_at_time(video_path, time_sec, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Cannot open video file: {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = int(fps * time_sec)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print(f"Saved frame at {time_sec}s to {output_path}")
    else:
        print(f"Failed to extract frame at {time_sec}s")
    cap.release()

if __name__ == "__main__":
    video_file = "download/soccer.mkv"
    save_frame_at_time(video_file, 6, "photo/soccer_6s.png")
    save_frame_at_time(video_file, 7, "photo/soccer_7s.png")