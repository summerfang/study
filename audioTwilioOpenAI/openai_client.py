# openai_client.py
import websockets

async def connect_openai_audio_stream():
    return await websockets.connect(
        "wss://api.openai.com/v1/audio/transcriptions",
        extra_headers={"Authorization": f"Bearer {config.OPENAI_KEY}"}
    )
