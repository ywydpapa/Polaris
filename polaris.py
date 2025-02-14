# 프로젝트 폴라리스 - 추적 매매 시스템
import asyncio
import time


async def slot1_main():
    print('Slot1 main loop start')
    await asyncio.sleep(1)
    print('Slot1 main loop stop')

async def slot2_main():
    print('Slot2 main loop start')
    await asyncio.sleep(3)
    print('Slot2 main loop stop')

async def slot3_main():
    print('Slot3 main loop start')
    await asyncio.sleep(1)
    print('Slot3 main loop stop')

async def slot4_main():
    print('Slot4 main loop start')
    await asyncio.sleep(2)
    print('Slot4 main loop stop')

async def main():
    await asyncio.gather(slot1_main(), slot2_main())
    await asyncio.gather(slot3_main(), slot4_main())

cnt = 1
while True:
    print(cnt)
    asyncio.run(main())
    cnt += 1

