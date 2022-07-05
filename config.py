import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')