import os
import subprocess

def merge_video_segments(extracted_clips_dir, merged_videos_dir, merged_video_filename='merged_video.mp4'):
    # Directory to save the merged video
    os.makedirs(merged_videos_dir, exist_ok=True)
    for filename in os.listdir(merged_videos_dir):
        file_path = os.path.join(merged_videos_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Path to the output merged video file
    merged_video = os.path.join(merged_videos_dir, merged_video_filename)

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

    print("Video segments merged successfully.")

# Example usage
# extracted_clips_dir = 'extracted_clips'
# merged_videos_dir = 'merged_videos'
# merge_video_segments(extracted_clips_dir, merged_videos_dir)
