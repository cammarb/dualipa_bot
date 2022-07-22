from os import set_inheritable
import requests
from config import CX, API
import random

# print(json_dict)
arraySize = 10

def search_image_links():
    link = f"https://customsearch.googleapis.com/customsearch/v1?cx={CX}&imgType=photo&{arraySize}&q=dua%20lipa&searchType=image&start=1&prettyPrint=true&key={API}"

    response = requests.get(link)
    json_dict = response.json()

    links_arrays = []

    for image in json_dict["items"]:
        links_arrays.append(image.get('link'))

    pic = random.choice(links_arrays)

    return pic

