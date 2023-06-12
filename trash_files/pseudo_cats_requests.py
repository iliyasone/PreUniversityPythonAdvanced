from random import random
import asyncio
import aiohttp

import os

from funct_test import time_measure




# async_request более простыми словами
async def async_request():
    link = "https://api.thecatapi.com/v1/images/search?limit=10"
    
    session = aiohttp.ClientSession()
    response = await session.get(link)
   
    answer: list[dict[str, str | int]] = await response.json()
    await response.release()
    tasks = []
    
    for i in range(10):
    
        img_url = answer[i]['url']
        tasks.append(download_cat(session, img_url, i))
    
    await asyncio.gather(*tasks)
    
    await session.close()

async def download_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    response = await session.get(img_url)
    img = await response.read()
    
    format = img_url[-3:]
        
    
    file = open(f'cats/cat{i+1}.{format}', 'wb')
    
    print(file.name)
    file.write(img)
    file.close()
        
    #await response.release()



import os
for file in os.listdir('cats'):
    os.remove('cats/'+file)





async def pseudo_sync_request():
    link = ...
    session = ...
    
    for i in range(10):
        img_url = ...
        await pseudo_download_cat(session, img_url, i)
    print("Done")
    
async def pseudo_async_request():
    link = ...
    session = ...
    
    for i in range(10):
        img_url = ...
        await pseudo_download_cat(session, img_url, i)
    print("Done")

async def pseudo_download_cat(session, img_url, i: int):
    await asyncio.sleep(random()*1.2)     
    print(f"cat{i+1}.png")
    



@time_measure
def async_main():
    asyncio.run(async_request())
   
@time_measure
def pseudo_async_main():
    asyncio.run(pseudo_async_request()) 

async_main()