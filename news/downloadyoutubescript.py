import sys
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    response = request.execute()
    if not response['items']:
        print("Video not found")
        sys.exit(1)
    snippet = response['items'][0]['snippet']
    channel = snippet['channelTitle']
    publish_date = datetime.strptime(snippet['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
    return channel, publish_date

def download_transcript(url):
    try:
        yt = YouTube(url)
        video_id = yt.video_id
        channel, publish_date = get_video_details(video_id)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'zh'])
        filename = f"{channel}_{publish_date.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for entry in transcript:
                f.write(f"{entry['start']}: {entry['text']}\n")
        print(f"Transcript saved to {filename}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python downloadyoutubescript.py <YouTube_URL>")
    else:
        download_transcript(sys.argv[1])