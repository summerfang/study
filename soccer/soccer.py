import os
import sys
import shutil
import requests
from preconditions import ensure_preconditions
from download_and_extract import download_youtube_video
from extract_video_segments import extract_video_segments
from merge_video_segments import merge_video_segments

def print_usage():
    print("Usage:")
    print("  python soccer.py https://www.youtube.com/watch?v=xxxx")
    print("  python soccer.py https://www.youtube.com/watch?v=xxxx output_file.mp4")
    print("  python soccer.py input_file.mp4 output_file.mp4")
    print("or set up a .env file with:")
    print("  YOUTUBE_URL=https://www.youtube.com/watch?v=xxxx")
    print("or set up the environment variable:")
    print("  export YOUTUBE_URL=https://www.youtube.com/watch?v=xxxx")

def verify_youtube_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200 and "text/html" in response.headers["Content-Type"]:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def main(input_source, output_file='merged_video.mp4'):
    # Determine if input is a URL or a local file
    if input_source.startswith("https://"):
        download_youtube_video(input_source)
        # Get the downloaded video file
        download_folder = "download"
        video_files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]
        if not video_files:
            print("No video files found in the download folder.")
            exit(1)
        input_video = os.path.join(download_folder, video_files[0])
    else:
        # Input is a local file
        if not os.path.exists(input_source):
            print(f"Input file {input_source} does not exist.")
            exit(1)
        input_video = input_source

    # Extract video segments
    extract_video_segments(input_video)

    # Merge video segments
    merged_videos_dir = 'merged_videos'
    shutil.rmtree(merged_videos_dir, ignore_errors=True)
    os.makedirs(merged_videos_dir, exist_ok=True)
    extracted_clips_dir = 'extracted_clips'
    merge_video_segments(extracted_clips_dir, merged_videos_dir, output_file)

if __name__ == "__main__":
    preconditions_status = ensure_preconditions()
    if preconditions_status is None:
        exit(1)

    if len(sys.argv) > 1:
        input_source = sys.argv[1]
        output_file = 'merged_video.mp4'  # Default output filename
        
        # If input is a URL, verify it
        if input_source.startswith("https://"):
            if not input_source.startswith("https://www.youtube.com/") or not verify_youtube_url(input_source):
                print("Invalid YouTube URL format or the URL is not valid.")
                print_usage()
                exit(1)
        # If input is a file, check if it exists
        elif not os.path.exists(input_source):
            print(f"Input file {input_source} does not exist.")
            print_usage()
            exit(1)
        
        # If second parameter is provided, use it as output filename
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
        
        main(input_source, output_file)
    else:
        # No command line arguments, try environment variable
        youtube_url = os.getenv("YOUTUBE_URL")
        if not youtube_url or not verify_youtube_url(youtube_url):
            print("YOUTUBE_URL environment variable is not set or the URL is not valid.")
            print_usage()
            exit(1)
        main(youtube_url)