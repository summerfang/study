import os
import sys
import argparse
import logging
import shutil
from datetime import datetime, timedelta
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import dl_yt_dlp  # Import the dl_yt_dlp module
import extract_audio  # Import the extract_audio module
import audio2text  # Import the audio2text module
import market_trend  # Import the market_trend module
from summarize_gemini import summarize_file_in_chinese  # Import the summarize_gemini module

# Load environment variables from .env file
load_dotenv()

# Set up YouTube Data API credentials using GOOGLE_API_KEY
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Error: GOOGLE_API_KEY not found in environment variables.")
    sys.exit(1)

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_channel_id(channel_name):
    """
    Retrieve the channel ID for a given YouTube channel name.

    Args:
        channel_name (str): The name of the YouTube channel.

    Returns:
        str: The channel ID if found, else None.
    """
    try:
        request = youtube.search().list(
            part='snippet',
            q=channel_name,
            type='channel',
            maxResults=1
        )
        response = request.execute()
        items = response.get('items', [])
        if not items:
            print(f"No channel found for: {channel_name}")
            return None
        return items[0]['snippet']['channelId']
    except HttpError as e:
        print(f"An HTTP error occurred while fetching channel ID for '{channel_name}': {e}")
        return None

def get_latest_video_info(channel_id):
    """
    Get the publication date and video ID of the latest video for a given channel ID.

    Args:
        channel_id (str): The YouTube channel ID.

    Returns:
        dict: A dictionary with 'publishedAt' and 'videoId' keys if available, else None.
    """
    try:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            order='date',
            maxResults=1,
            type='video'
        )
        response = request.execute()
        items = response.get('items', [])
        if not items:
            print(f"No videos found for channel ID: {channel_id}")
            return None
        video_info = {
            'publishedAt': items[0]['snippet']['publishedAt'],
            'videoId': items[0]['id']['videoId']
        }
        return video_info
    except HttpError as e:
        print(f"An HTTP error occurred while fetching videos for channel ID '{channel_id}': {e}")
        return None

def is_valid_url(url):
    """
    Validate the URL format.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def load_channel_names(file_path):
    """
    Load channel names from a text file, one per line.

    Args:
        file_path (str): Path to the channels.txt file.

    Returns:
        list: A list of channel names.
    """
    if not os.path.exists(file_path):
        print(f"Channel list file not found: {file_path}")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def has_new_video_today(channel_names):
    """
    Check if the listed YouTube channels have uploaded a new video in the last 24 hours.

    Args:
        channel_names (list): A list of YouTube channel names.

    Returns:
        dict: A dictionary with channel names as keys and details of new uploads if any.
    """
    results = {}
    last_24h = datetime.utcnow() - timedelta(hours=24)

    for name in channel_names:
        print(f"Checking channel: {name}")
        channel_id = get_channel_id(name)
        if not channel_id:
            results[name] = {"has_new_video": False, "video_url": None}
            continue
        latest_video_info = get_latest_video_info(channel_id)
        if not latest_video_info:
            results[name] = {"has_new_video": False, "video_url": None}
            continue
        # Parse the publication date
        video_date_str = latest_video_info['publishedAt']
        video_date = datetime.strptime(video_date_str, "%Y-%m-%dT%H:%M:%SZ")
        has_new = video_date >= last_24h
        video_url = f"https://www.youtube.com/watch?v={latest_video_info['videoId']}" if has_new else None
        results[name] = {"has_new_video": has_new, "video_url": video_url}
    return results

def main():
    parser = argparse.ArgumentParser(description="Check for new YouTube videos from subscribed channels.")
    parser.add_argument(
        "-f", "--file",
        type=str,
        default="channels.txt",
        help="Path to the text file containing YouTube channel names, one per line."
    )
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    channel_names = load_channel_names(args.file)
    if not channel_names:
        print("No channel names to check.")
        sys.exit(1)

    new_videos = has_new_video_today(channel_names)
    channel_trends = {}  # Dictionary to store market trends per channel

    for channel, info in new_videos.items():
        if info["has_new_video"]:
            print(f"Channel '{channel}' has a new video today: {info['video_url']}")
            downloaded_video_path = dl_yt_dlp.download_video(info["video_url"])  # Returns a single file path
            if downloaded_video_path:
                # Extract audio from the downloaded video
                audio_file_path = extract_audio.extract_audio(downloaded_video_path)
                if audio_file_path and os.path.exists(audio_file_path):
                    print(f"Audio extracted successfully: {audio_file_path}")
                    
                    # Convert audio to text with Chinese language support
                    transcription = audio2text.transcribe_audio(audio_file_path, language='zh')
                    if transcription:
                        # Define the transcription output path
                        txt_output_path = f"{os.path.splitext(audio_file_path)[0]}.txt"
                        audio2text.save_transcription(transcription, txt_output_path)
                        print(f"Transcription saved successfully: {txt_output_path}")
                        
                        # Analyze market trend from transcription
                        trend = market_trend.determine_trend(transcription)
                        channel_trends[channel] = trend
                        print(f"Market trend for '{channel}': {trend}")
                        
                        # Generate and save summary
                        summary_file_path = f"{os.path.splitext(audio_file_path)[0]}.summary.txt"
                        try:
                            summary = summarize_file_in_chinese(txt_output_path)
                            with open(summary_file_path, 'w', encoding='utf-8') as f:
                                f.write(summary)
                            print(f"Summary saved successfully: {summary_file_path}")
                            channel_trends[channel] = {"trend": trend, "summary": summary}
                        except Exception as e:
                            logging.error(f"Failed to generate summary for {channel}: {e}")
                            channel_trends[channel] = {"trend": trend, "summary": "Summary generation failed"}
                        
                        # Define archive directory based on current date and channel name
                        today = datetime.utcnow()
                        archive_dir = os.path.join(
                            "archive",
                            str(today.year),
                            str(today.month),
                            str(today.day),
                            channel.replace(" ", "_")
                        )
                        os.makedirs(archive_dir, exist_ok=True)
                        
                        # Copy audio, transcript, and summary files to the archive directory
                        try:
                            shutil.copy2(audio_file_path, archive_dir)
                            shutil.copy2(txt_output_path, archive_dir)
                            shutil.copy2(summary_file_path, archive_dir)
                            print(f"Files archived to: {archive_dir}")
                        except Exception as e:
                            logging.error(f"Failed to archive files for {channel}: {e}")
                    else:
                        print(f"Transcription failed for: {audio_file_path}")
                        channel_trends[channel] = {"trend": "Transcription Failed", "summary": None}
                else:
                    print(f"Audio extraction failed for: {downloaded_video_path}")
                    channel_trends[channel] = {"trend": "Audio Extraction Failed", "summary": None}
        else:
            print(f"Channel '{channel}' has no new videos today.")
            channel_trends[channel] = {"trend": "No new video", "summary": None}

    # After processing all channels, list the market trends with summaries
    print("\n=== Market Trends and Summaries ===")
    for channel, info in channel_trends.items():
        print(f"\nChannel: '{channel}'")
        print(f"Trend: {info['trend']}")
        if info['summary']:
            print("Summary:")
            print(info['summary'])
        print("-" * 50)

if __name__ == "__main__":
    main()