from .config import *
from .google_search import search_image_links

import discord
from discord.ext import commands

def my_test():
    return 'my message'

def create_bot():
    # DISCORD
    bot = commands.Bot(command_prefix='/')
    client = discord.Client()

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="Levitating", url="https://www.youtube.com/watch?v=TUVcZfQe-Kw"))
        print("Dua Lipa Bot is ready.")

    @bot.command(name='dua random')
    async def dua(ctx, extra):
        await ctx.send(search_image_links(extra))
    
    @bot.command(name='dua bikini')
    async def dua(ctx, extra):
        await ctx.send(search_image_links("bikini"))

    # We can call the command by its name as an decorator
    @dua.error
    async def dua_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Oh no, something happened. Please enter the command again.", file=discord.File('bot/img/dua_troste.png'))

    # TODO: slash commands
    # @bot.slash_command(name='test', description='this is a test', guild = discord.Object(GUILD))
    # async def test(interaction: discord.intera):
    #     await interaction.response.send_message('hello, this is a test')

    bot.run(TOKEN)