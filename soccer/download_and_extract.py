import subprocess
import os
import shutil
from extract_video_segments import extract_video_segments
from merge_video_segments import merge_video_segments

def download_youtube_video(url):
    yt_dlp_path = os.getenv("YT_DLP_PATH", "yt-dlp")
    download_folder = "download"
    shutil.rmtree(download_folder, ignore_errors=True)
    os.makedirs(download_folder, exist_ok=True)
    subprocess.run([yt_dlp_path, "-o", os.path.join(download_folder, "%(title)s.%(ext)s"), url])

if __name__ == "__main__":
    youtube_url = "https://youtu.be/bzOWTiV7YCA?si=TTlzc3EA5ZgHFyf-"
    download_youtube_video(youtube_url)

    # Get the downloaded video file
    download_folder = "download"
    video_files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]
    if not video_files:
        print("No video files found in the download folder.")
        exit(1)
    downloaded_video = os.path.join(download_folder, video_files[0])

    # Extract video segments
    extract_video_segments(downloaded_video)

    # Merge video segments
    merged_videos_dir = 'merged_videos'
    shutil.rmtree(merged_videos_dir, ignore_errors=True)
    os.makedirs(merged_videos_dir, exist_ok=True)
    extracted_clips_dir = 'extracted_clips'
    merge_video_segments(extracted_clips_dir, merged_videos_dir, 'merged_video.mp4')