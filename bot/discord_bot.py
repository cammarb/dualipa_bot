from os import name
from .config import *
from .google_search import search_image_links

import random

import discord
from discord.ext import commands

def my_test():
    return 'my message'

def create_bot():
    # DISCORD
    bot = commands.Bot(command_prefix='!')
    client = discord.Client()

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="Levitating", url="https://www.youtube.com/watch?v=TUVcZfQe-Kw"))
        print("Dua Lipa Bot is ready.")

    @bot.command(name='dua')
    async def photos(ctx, *, extra:str):
        await ctx.send(search_image_links(extra))

    bot.run(TOKEN)