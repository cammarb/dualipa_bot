from config import *
from google_search import search_image_links

import random

import discord
from discord.ext import commands

def create_bot():
    # DISCORD
    bot = commands.Bot(command_prefix='!')
    client = discord.Client()

    @bot.command(name='dua')
    async def photos(ctx):
        await ctx.send(search_image_links())

    bot.run(TOKEN)

create_bot()