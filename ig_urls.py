from config import *
import json
import instaloader

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')

# INSTAGRAM
L = instaloader.Instaloader()
L.login(USER, PASSWORD)

profile = instaloader.Profile.from_username(L.context, 'dualipa')

# JSON
urls = []

for index, post in enumerate(profile.get_posts()):
    urls.append(post.url)

with open('posts_url.json', 'w') as outfile:
    json.dump(urls, outfile)