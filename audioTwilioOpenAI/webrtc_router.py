# webrtc_router.py
from fastapi import WebSocket, APIRouter

router = APIRouter()

class WebRTCManager:
    def __init__(self):
        self.connections = {}
        self.audio_buffers = {}

    async def handle_webrtc(self, websocket: WebSocket):
        await websocket.accept()
        client_id = str(uuid.uuid4())
        
        # 初始化OpenAI连接
        openai_ws = await connect_openai_audio_stream()
        
        async def forward_to_openai(data: bytes):
            await openai_ws.send_bytes(data)
        
        async def receive_from_openai():
            async for response in openai_ws.iter_bytes():
                await websocket.send_bytes(response)
        
        try:
            while True:
                data = await websocket.receive_bytes()
                await forward_to_openai(data)
                
        except WebSocketDisconnect:
            await openai_ws.close()
