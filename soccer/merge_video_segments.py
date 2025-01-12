import os
import subprocess

# Directory where the extracted clips are saved
extracted_clips_dir = 'extracted_clips'

# Directory to save the merged video
merged_videos_dir = 'merged_videos'

# Create the merged videos directory if it doesn't exist
os.makedirs(merged_videos_dir, exist_ok=True)

# Path to the output merged video file
merged_video = os.path.join(merged_videos_dir, 'merged_video.mp4')

# List all video files in the extracted_clips directory and sort by creation time
video_files = sorted(
    [f for f in os.listdir(extracted_clips_dir) if f.endswith('.mp4')],
    key=lambda f: os.path.getctime(os.path.join(extracted_clips_dir, f))
)

# Path to the temporary file list
file_list_path = 'file_list.txt'

# Write the list of video files to the temporary file
with open(file_list_path, 'w') as file_list:
    for video_file in video_files:
        file_list.write(f"file '{os.path.join(extracted_clips_dir, video_file)}'\n")

# Construct the FFmpeg command to merge the video files
ffmpeg_command = [
    'ffmpeg',
    '-f', 'concat',
    '-safe', '0',
    '-i', file_list_path,
    '-c', 'copy',
    merged_video
]

# Run the FFmpeg command
subprocess.run(ffmpeg_command)

# Remove the temporary file list
os.remove(file_list_path)

print("Video merging completed.")
