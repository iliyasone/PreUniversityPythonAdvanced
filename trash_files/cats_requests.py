from __future__ import annotations
from funct_test import time_measure
import requests


@time_measure
def download_cats():
    link = "https://api.thecatapi.com/v1/images/search?limit=10"

    answer: list[dict[str, str | int]] \
        = requests.get(link).json()

    for i in range(10):
        
        img_url = answer[i]['url']
        img = requests.get(img_url).content
        
        format = img_url[-3:]
        
        with open(f'cat{i+1}.{format}', 'wb') as file:
            print(file.name)
            file.write(img)
    
download_cats()
