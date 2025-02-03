import os
import subprocess
import argparse
import sys
import logging
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Validate the URL format.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def extract_audio(video_path, audio_ext='mp3'):
    """
    Extract audio from a video file using ffmpeg.

    Args:
        video_path (str): Full path to the video file.
        audio_ext (str): Desired audio file extension (default: 'mp3').

    Returns:
        str: Full path to the extracted audio file or None if failed.
    """
    if not os.path.isfile(video_path):
        logging.error(f"Video file not found: {video_path}")
        return None

    base, _ = os.path.splitext(video_path)
    audio_path = f"{base}.{audio_ext}"

    # Define ffmpeg command to extract audio and convert to desired format
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vn',  # No video
        '-acodec', 'libmp3lame' if audio_ext == 'mp3' else 'copy',
        '-y',  # Overwrite output file if it exists
        audio_path
    ]

    try:
        logging.info(f"Starting audio extraction: {audio_path}")
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Audio extracted successfully: {audio_path}")
        return audio_path
    except subprocess.CalledProcessError as e:
        logging.error(f"ffmpeg error: {e.stderr.decode().strip()}")
        return None
    except FileNotFoundError:
        logging.error("ffmpeg not found. Please ensure it is installed and added to the system PATH.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Extract audio from a video file using ffmpeg.")
    parser.add_argument('video_path', type=str, help='Full path to the video file.')
    parser.add_argument('-e', '--extension', type=str, default='mp3', help='Audio file extension (default: mp3).')
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # if not is_valid_url(args.video_path):
    #     logging.error("Invalid video file path or URL.")
    #     sys.exit(1)

    audio_file = extract_audio(args.video_path, args.extension)
    if audio_file:
        print(f"Audio extracted to: {audio_file}")
    else:
        print("Audio extraction failed.")

if __name__ == "__main__":
    main()