import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("TWo")


async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())
