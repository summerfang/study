import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
audio_file = open("audio.mp3", "rb")
openai.Audio.transcribe('whisper-1', audio_file)