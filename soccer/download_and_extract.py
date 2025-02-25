import subprocess
import os
import shutil
import importlib.util

from extract_video_segments import extract_video_segments
from merge_video_segments import merge_video_segments

def download_youtube_video(url):
    download_folder = "download"
    shutil.rmtree(download_folder, ignore_errors=True)
    os.makedirs(download_folder, exist_ok=True)

    # Check if yt-dlp is installed as a Python library
    yt_dlp_spec = importlib.util.find_spec("yt_dlp")
    if yt_dlp_spec is not None:
        import yt_dlp
        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        yt_dlp_path = os.getenv("YT_DLP_PATH", "yt-dlp")
        if not shutil.which(yt_dlp_path):
            print(f"yt-dlp executable not found at {yt_dlp_path}. Please install yt-dlp or set the YT_DLP_PATH environment variable.")
            exit(1)
        subprocess.run([yt_dlp_path, "-o", os.path.join(download_folder, "%(title)s.%(ext)s"), url])
