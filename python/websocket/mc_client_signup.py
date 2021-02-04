import asyncio
import websockets
import json

async def connect():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        signup_message = {
            "version": "1",
            "action": "signup",
            "name": "Summer Fang",
            "password": "xyz1999"
        }

        signup_data = json.dumps(signup_message)
        await websocket.send(signup_data)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())