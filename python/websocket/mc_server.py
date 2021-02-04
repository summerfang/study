import asyncio
import websockets
import json

websocket_set = set()

async def signup(user, password):
    print(f'User={user},password={password}')

async def register(websocket):
    websocket_set.add(websocket)

async def unregister(websocket):
    websocket_set.remove(websocket)

async def login(user, password):
    pass


async def mc_main(websocket, path):
    await register(websocket)

    try:
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "signup":
                user = data["name"]
                password = data["password"]
                await signup(user, password)
            elif data["action"] == "login":
                user = data["name"]
                password = data["password"]
                await login(user, password)
            elif data["action"] == "create_meeting":
                pass
            elif data["action"] == "":
                pass
            elif data["action"] == "":
                pass
            else:
                pass

        if path == "signup":
            await signup()

    finally:
        await unregister(websocket)

if __name__ == "__main__":
    start_server = websockets.serve(mc_main, "localhost", 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()