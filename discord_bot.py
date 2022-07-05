from config import *
import random
import json

import discord
from discord.ext import commands

# READ JSON FILE
with open("posts_url.json") as f:
    urls = json.loads(f.read())

# DISCORD
bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.command(name='dua')
async def photos(ctx):
    # for downloaded pictures
    # pic = str(random.choice(os.listdir("dualipa")))
    # await ctx.send(file=discord.File('dualipa/'+pic))

    await ctx.send(random.choice(urls))


bot.run(TOKEN)