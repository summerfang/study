import pytube
import moviepy.editor as mp
import speech_recognition as sr
import logging

logging.basicConfig(level=logging.INFO)

def download_video(url):
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        output_path = stream.download(filename="video.mp4")
        return output_path
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        return None

def extract_audio(video_path):
    try:
        clip = mp.VideoFileClip(video_path)
        audio_path = video_path.replace(".mp4", ".wav")
        clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
        return audio_path
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        return None

def transcribe_audio(audio_path):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        return None

def main(url):
    video_path = download_video(url)
    if video_path:
        audio_path = extract_audio(video_path)
        if audio_path:
            transcript = transcribe_audio(audio_path)
            if transcript:
                print("Transcript:\n", transcript)
            else:
                logging.error("Transcription failed.")
        else:
            logging.error("Audio extraction failed.")
    else:
        logging.error("Video download failed.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    main(video_url)
