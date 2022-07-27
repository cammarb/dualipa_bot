import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API = os.getenv('GOOGLE_API')
CX = os.getenv('SEARCH_CX')
GUILD = os.getenv('GUILD_ID')