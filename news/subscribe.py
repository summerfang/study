import os
import sys
import argparse
import logging
import shutil
from datetime import datetime, timedelta
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dl_yt_dlp import download_video
from extract_audio import extract_audio
from audio2text import transcribe_audio
from summarize_gemini import summarize_file_in_chinese
# import market_trend

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

def get_recent_videos(channel_id):
    """Get all videos from last 24 hours for a channel."""
    videos = []
    try:
        now = datetime.utcnow()
        yesterday = now - timedelta(days=1)
        
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            maxResults=50,
            publishedAfter=yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')
        )
        response = request.execute()
        
        for item in response['items']:
            if item['id'].get('videoId'):
                video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
                videos.append({
                    'url': video_url,
                    'title': item['snippet']['title'],
                    'publishedAt': item['snippet']['publishedAt']
                })
    except Exception as e:
        logging.error(f"Error getting videos for channel {channel_id}: {e}")
    return videos

def clear_downloads_folder():
    """Clear all files in the downloads folder."""
    downloads_dir = "downloads"
    if os.path.exists(downloads_dir):
        for file in os.listdir(downloads_dir):
            file_path = os.path.join(downloads_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error: {e}")

def process_video(video, channel_name):
    """Process a single video: download, transcribe, summarize, and analyze trend."""
     # Clear downloads folder before processing new video
    clear_downloads_folder()
    
    result = {
        'title': video['title'],
        'timestamp': video['publishedAt'],
        'trend': None,
        'summary': None
    }
    
    try:
        # 
        # Download video using dl_yt_dlp
        downloaded_video_path = download_video(video['url'])
        if not downloaded_video_path:
            raise Exception("Video download failed")

        # Extract audio using extract_audio module
        audio_file_path = extract_audio(downloaded_video_path)
        if not audio_file_path:
            raise Exception("Audio extraction failed")

        # Transcribe using audio2text module
        transcription = transcribe_audio(audio_file_path)
        if not transcription:
            raise Exception("Transcription failed")

        # Save transcription
        txt_output_path = f"{os.path.splitext(audio_file_path)[0]}.txt"
        with open(txt_output_path, 'w', encoding='utf-8') as f:
            f.write(transcription)

        # Generate summary using summarize_file_in_chinese
        result['summary'] = summarize_file_in_chinese(txt_output_path)
        # result['trend'] = market_trend.determine_trend(transcription)

        # Add new summary file path
        summary_file = f"{os.path.splitext(audio_file_path)[0]}.summary.txt"

        # Write summary to the new file
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(result['summary'])
            # f.write(result['trend'])

        # Move both files to archive
        # archive_path = os.path.join(archive_dir, os.path.basename(txt_output_path))
        # archive_summary_path = os.path.join(archive_dir, os.path.basename(summary_file))

        # # Move original file and summary file
        # shutil.move(txt_output_path, archive_path)
        # shutil.move(summary_file, archive_summary_path)

        # Archive files
        video_id = video['url'].split('=')[-1]
        archive_dir = os.path.join(
            "archive",
            datetime.utcnow().strftime("%Y/%m/%d"),
            channel_name.replace(" ", "_"),
            video_id
        )
        os.makedirs(archive_dir, exist_ok=True)
        
        # Copy files to archive
        for file_path in [audio_file_path, txt_output_path, summary_file, downloaded_video_path]:
            if os.path.exists(file_path):
                shutil.copy2(file_path, archive_dir)

        # Cleanup temporary files
        if os.path.exists(downloaded_video_path):
            os.remove(downloaded_video_path)
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
        if os.path.exists(summary_file):
            os.remove(summary_file)
        if os.path.exists(downloaded_video_path):
            os.remove(downloaded_video_path)

    except Exception as e:
        logging.error(f"Error processing video {video['title']}: {e}")
        result['error'] = str(e)

    return result

def get_channels(channel_names):
    """Get channel IDs for given channel names."""
    channels = {}
    for channel in channel_names:
        try:
            request = youtube.search().list(
                part="id,snippet",
                q=channel,
                type="channel",
                maxResults=1
            )
            response = request.execute()
            
            if response['items']:
                channel_id = response['items'][0]['id']['channelId']
                channels[channel] = channel_id
                
        except Exception as e:
            logging.error(f"Error getting channel ID for {channel}: {e}")
    return channels

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

    # Get channels
    channels = get_channels(channel_names)
    if not channels:
        print("No channels found.")
        return

    # Process each channel
    all_results = {}
    for channel_name, channel_id in channels.items():
        print(f"\nProcessing channel: {channel_name}")
        
        # Get recent videos
        videos = get_recent_videos(channel_id)
        if not videos:
            print(f"No new videos found for channel {channel_name}")
            continue
            
        print(f"Found {len(videos)} videos in the last 24 hours")
        
        # Process each video
        channel_results = []
        for video in videos:
            print(f"Processing video: {video['title']}")
            result = process_video(video, channel_name)
            channel_results.append(result)
            
        all_results[channel_name] = channel_results

    # Output final results
    print("\n=== Market Trends and Summaries ===")
    for channel, results in all_results.items():
        print(f"\nChannel: {channel}")
        if not results:
            print("No videos processed")
            continue
            
        for result in results:
            print(f"\nVideo: {result['title']}")
            print(f"Published at: {result['timestamp']}")
            # print(f"Market Trend: {result['trend']}")
            if result['summary']:
                print("Summary:")
                print(result['summary'])
            if result.get('error'):
                print(f"Error: {result['error']}")
            print("-" * 30)
        print("=" * 50)

if __name__ == "__main__":
    main()