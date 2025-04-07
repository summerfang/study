# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import openai
from starlette.responses import StreamingResponse
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 实时流式响应端点
@app.post("/stream")
async def stream_response(prompt: str):
    try:
        return StreamingResponse(
            generate_openai_stream(prompt),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e))

# 流生成器
async def generate_openai_stream(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        stream=True
    )
    
    async for chunk in response:
        content = chunk.choices[0].delta.get("content", "")
        if content:
            yield f"data: {content}\n\n"

# # main.py
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# import websockets
# import json
# import os

# app = FastAPI()

# # Mount the static files directory
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def read_index():
#     return FileResponse('static/index.html')

# @app.websocket("/ws/openai")
# async def proxy_websocket(websocket: WebSocket):
#     await websocket.accept()
    
#     # 连接OpenAI实时API
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     openai_ws = await websockets.connect(
#         "wss://api.openai.com/v1/audio/realtime",
#         extra_headers={"Authorization": f"Bearer {OPENAI_API_KEY}"}
#     )
    
#     try:
#         while True:
#             # 双向数据转发
#             client_data = await websocket.receive_bytes()
#             await openai_ws.send(client_data)
            
#             openai_response = await openai_ws.recv()
#             await websocket.send_bytes(openai_response)
            
#     except Exception as e:
#         await openai_ws.close()
