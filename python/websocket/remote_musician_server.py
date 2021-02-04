import asyncio

meeting_session = {}

async def register(websocket, path):
    meeting_session[websocket] = {}

async def remote_musician_main(websocket, path): 
    await register(websocket, path)

    if path == '/signup':
        pass
    elif path == '/login':
        pass
    elif path == '/start_meeting':
        pass
    else:
        pass

if __name__ == "__main__":
    pass