import asyncio
import time

async def say_after(second, message):
    await asyncio.sleep(second)
    print(message)

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World!"))

    print(f'Start:{time.strftime("%X")}')
    await task1
    await task2
    print(f'End:{time.strftime("%X")}')

if __name__ == "__main__":
    asyncio.run(main())