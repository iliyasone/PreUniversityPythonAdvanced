import asyncio
from random import random
import aiohttp

from funct_test import time_measure # НЕ ДЛЯ ВАС!!!

# удаление из cats/
import os
for file in os.listdir('cats'):
    os.remove('cats/'+file)

async def download_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    response = await session.get(img_url)
    img_bytes = await response.read()
    
    format = img_url[-3:]
    
    file = open(f'cats/cat{i+1}.{format}', "wb")
    file.write(img_bytes)
    file.close()
    
    print(f"cat{i+1}.{format}")
    

async def request():
    link = "https://api.thecatapi.com/v1/images/search?limit=10"
    
    session = aiohttp.ClientSession()
    
    
    response = await session.get(link)
    answer: list[dict[str, str | int]] = await response.json()
    
    tasks = []
        
    for i in range(10):
        img_url = answer[i]['url']
        tasks.append(download_cat(session, img_url, i))
    await asyncio.gather(*tasks)
    
    await session.close()


@time_measure # НЕ ДЛЯ ВАС
def main():
    asyncio.run(request())
    
main()

    

    
    
