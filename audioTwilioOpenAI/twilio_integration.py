# twilio_integration.py
from twilio.rest import Client
from fastapi import APIRouter

router = APIRouter()

@router.websocket("/twilio-media")
async def handle_twilio_stream(websocket: WebSocket):
    await websocket.accept()
    openai_ws = await connect_openai()  # 复用之前的连接方法
    
    async def process_media(payload: dict):
        if payload['event'] == 'media':
            audio = base64.b64decode(payload['media']['payload'])
            processed = await AudioConverter.twilio_to_openai(audio)
            await openai_ws.send(processed)

    try:
        while True:
            data = await websocket.receive_json()
            await process_media(data)
            
            # 转发OpenAI响应到电话
            response = await openai_ws.recv()
            await websocket.send_json({
                "event": "media",
                "media": {
                    "payload": base64.b64encode(response).decode(),
                    "type": "audio/wav"
                }
            })
    finally:
        await openai_ws.close()
