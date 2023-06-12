from __future__ import annotations
import aiohttp
import asyncio

from time import time, sleep

def time_measure(func):
    def wrapper(*args, **kwargs):
        before_execute = time()
        result = func(*args, **kwargs)
        after_exectute = time()
        print(f'{func.__name__} was called for {after_exectute - before_execute}')
        return result
    return wrapper


async def async_request():
    link = "https://api.thecatapi.com/v1/images/search?limit=10"
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            answer: list[dict[str, str | int]] = await response.json()
            
            tasks = []
            
            for i in range(10):
            
                img_url = answer[i]['url']
                tasks.append(download_cat(session, img_url, i))
            
            await asyncio.gather(*tasks)

async def download_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    async with session.get(img_url) as response:
        img = await response.read()
        
        format = img_url[-3:]
        
        with open(f'cat{i+1}.{format}', 'wb') as file:
            print(file.name)
            file.write(img)


@time_measure
def main():
    asyncio.run(async_request())
main()