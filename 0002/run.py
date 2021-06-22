import asyncio
import random
import time


warehouse = []
max_elements = 10


def is_overflow() -> bool:
    return len(warehouse) >= max_elements


def is_underflow() -> int:
    return len(warehouse) == 0


async def producer() -> None:
    x = random.randint(a=1, b=10000)
    print('produced number {}'.format(x))
    if not is_overflow():
        warehouse.append(x)
    else:
        await consumer()
        print("Overflow. Producer waiting")


async def consumer() -> None:
    if not is_underflow():
        x = warehouse.pop(0)
        print('consumed number {}'.format(x))
    else:
        await producer()
        print("Underflow. Consumer waiting")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(asyncio.gather(asyncio.Task(producer()), asyncio.Task(consumer())))
        time.sleep(1)
