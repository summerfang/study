import asyncio
from asyncio.tasks import sleep

async def main():
    print("Hello")
    await sleep(1) # Can only use asyncio's sleep
    print("World!")

if __name__ == "__main__":
    asyncio.run(main())