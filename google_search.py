import requests
from config import CX, API

# print(json_dict)

def search_image_links():
    link = f"https://customsearch.googleapis.com/customsearch/v1?cx={CX}&imgType=photo&num=1&q=dua%20lipa&searchType=image&start=1&prettyPrint=true&key={API}"

    response = requests.get(link)
    json_dict = response.json()

    for image in json_dict["items"]:
        return image.get('link')
 