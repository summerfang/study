import os
import av

VIDEO_FILE = os.path.join("download", "soccer.mkv")
OUTPUT_DIR = "I-Frame"
os.makedirs(OUTPUT_DIR, exist_ok=True)

container = av.open(VIDEO_FILE)
frame_number = 0
for frame in container.decode(video=0):
    if frame.pict_type == 1:
        img_path = os.path.join(OUTPUT_DIR, f"{frame_number}.png")
        frame.to_image().save(img_path)
        print(f"Saved I-frame {frame_number} to {img_path}")
    else:
        print(f"Skipped non I-frame {frame_number}, {frame.pict_type}")
    frame_number += 1