import asyncio
import time
from time import sleep


# Execution time: ~7.5s
async def f1():
    for i in range(5):
        print(f'f1({i})')
        # sleep(1.5)
        await asyncio.sleep(1.5)


# Execution time: ~5s
async def f2():
    for i in range(5):
        print(f'f2({i})')
        # sleep(1)
        await asyncio.sleep(1)


# Execution time: ~12s
async def f3():
    for i in range(10):
        print(f'f3({i})')
        # sleep(1)
        await asyncio.sleep(1.2)


async def main():
    await asyncio.gather(
        f1(),
        f2(),
    )
    # await asyncio.gather(
    #     *[f1() for _ in range(100)]
    # )


# Sync 12.511952877044678
# Sync 7.505792617797852

start = time.time()
# main()
asyncio.run(main())

end = time.time()

print(end - start)
