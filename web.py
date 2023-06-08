import requests
import os

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result
    return wrapper


@measure_time
def download_cats():
    url = "https://api.thecatapi.com/v1/images/search?limit=10"
    response = requests.get(url)
    data = response.json()
    print(len(data))
    if not os.path.exists("cats"):
        os.makedirs("cats")
        
        
    for i in range(10):
        img_url = data[i]["url"]
        img_data = requests.get(img_url).content
    with open(f"cats/cat{i}.jpg", "wb") as file:
        file.write(img_data)
    print("Downloaded 10 cat images successfully!")
download_cats()