# twilio_router.py
from twilio.rest import Client
from fastapi import APIRouter, WebSocket

router = APIRouter()
twilio_client = Client(config.TWILIO_SID, config.TWILIO_AUTH_TOKEN)

@router.websocket("/twilio-audio")
async def twilio_audio_stream(websocket: WebSocket):
    await websocket.accept()
    openai_ws = await connect_openai_audio_stream()
    
    async def process_twilio_media(message: dict):
        if message['event'] == 'media':
            audio_data = base64.b64decode(message['media']['payload'])
            await openai_ws.send_bytes(audio_data)
    
    try:
        while True:
            message = await websocket.receive_json()
            await process_twilio_media(message)
            
            # 转发OpenAI响应到电话端
            async for response in openai_ws.iter_bytes():
                await websocket.send_json({
                    "event": "media",
                    "media": {"payload": base64.b64encode(response).decode()}
                })
                
    except WebSocketDisconnect:
        await openai_ws.close()
