import requests
from .config import CX, API
import random

# print(json_dict)
arraySize = 10

def generateIndex():
    i = random.randrange(1, 11)
    return i * 10 + 1

def search_image_links(extra):
    start = generateIndex()
    if extra != '':
        link = f"https://customsearch.googleapis.com/customsearch/v1?cx={CX}&imgType=photo&{arraySize}&q=dua%20lipa%20{extra}&searchType=image&start={start}&prettyPrint=true&key={API}"
    else:
        link = f"https://customsearch.googleapis.com/customsearch/v1?cx={CX}&imgType=photo&{arraySize}&q=dua%20lipa%20&searchType=image&start={start}&prettyPrint=true&key={API}"
        # print('test')

    response = requests.get(link)
    json_dict = response.json()

    links_arrays = []

    for image in json_dict["items"]:
        links_arrays.append(image.get('link'))

    pic = random.choice(links_arrays)

    return pic