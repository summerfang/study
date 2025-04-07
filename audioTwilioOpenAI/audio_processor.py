# audio_processor.py
from pydub import AudioSegment
import numpy as np

class AudioConverter:
    @staticmethod
    async def web_to_openai(data: bytes):
        """转换网页音频(Opus)到OpenAI需要的格式"""
        audio = AudioSegment.from_ogg(BytesIO(data))
        return audio.set_frame_rate(16000).export(format="wav").read()

    @staticmethod
    async def twilio_to_openai(data: bytes):
        """转换Twilio音频(PCMU)到OpenAI格式"""
        audio = AudioSegment.from_raw(
            BytesIO(data), 
            sample_width=2, 
            frame_rate=8000, 
            channels=1
        )
        return audio.set_frame_rate(16000).export(format="wav").read()
