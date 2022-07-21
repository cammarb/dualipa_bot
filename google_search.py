import requests
from config import *
link = f"https://customsearch.googleapis.com/customsearch/v1?cx={CX}&imgType=photo&num=1&q=dua%20lipa&searchType=image&start=1&prettyPrint=true&key={API}"

response = requests.get(link)
json_dict = response.json()
# print(json_dict)

for image in json_dict["items"]:
    print(image.get('link'))
