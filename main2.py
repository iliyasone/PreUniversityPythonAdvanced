import asyncio
from types import coroutine
MLTPR = 3

async def loundary():
    print("Поставили стирку")
    await asyncio.sleep(1*MLTPR)
    print("Стирка закончена")

async def cooking():
    print("Поставили щи")
    await asyncio.sleep(1*MLTPR)
    print("Щи готовы")
    
async def tea():
    print("Ставим чайник")
    await asyncio.sleep(0.15*MLTPR)
    print("Пьём чай (крутые)")

async def main():
    await asyncio.gather(loundary(), cooking(), tea())


print(isinstance(asyncio.gather(loundary(), cooking(), tea()), coroutine))
asyncio.run(asyncio.gather(loundary(), cooking(), tea()))