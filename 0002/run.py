import asyncio
import random


warehouse = []
max_elements = 10


def is_overflow():
    return len(warehouse) >= max_elements


def is_underflow():
    return len(warehouse) == 0


async def producer():
    x = random.randint(a=1, b=10000)
    print('produced number {}'.format(x))
    if not is_overflow():
        warehouse.append(x)
    else:
        print("Overflow. Producer waiting")
    await asyncio.sleep(1)


async def consumer():
    if not is_underflow():
        x = warehouse.pop(0)
        print('consumed number {}'.format(x))
    else:
        print("Underflow. Consumer waiting")
    await asyncio.sleep(1)


async def main():
    while True:
        await producer()
        await consumer()
        asyncio.sleep(2)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(main())
