import asyncio
import time

async def say_after(second, message):
    await asyncio.sleep(second)
    print(message)

async def main():
    print(f'time start:{time.strftime("%X")}')
    await say_after(1, "Hello")
    await say_after(2,"World!")
    print(f'time end:{time.strftime("%X")}')
if __name__ == "__main__":
    asyncio.run(main())