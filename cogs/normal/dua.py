import discord
from discord.ext import commands
import requests
import config
import random

# print(json_dict)
arraySize = 10

def generateIndex():
    i = random.randrange(1, 11)
    return i * 10 + 1

def search_image_links(extra):
    start = generateIndex()
    if extra != '':
        link = f"https://customsearch.googleapis.com/customsearch/v1?cx={config.CX}&imgType=photo&{arraySize}&q=dua%20lipa%20{extra}&searchType=image&start={start}&prettyPrint=true&key={config.API}"
    else:
        link = f"https://customsearch.googleapis.com/customsearch/v1?cx={config.CX}&imgType=photo&{arraySize}&q=dua%20lipa%20&searchType=image&start={start}&prettyPrint=true&key={config.API}"
        # print('test')

    response = requests.get(link)
    json_dict = response.json()

    links_arrays = []

    for image in json_dict["items"]:
        links_arrays.append(image.get('link'))

    pic = random.choice(links_arrays)

    return pic

class Dua(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dua cog loaded.')
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx):
        embed = discord.Embed(description="this is a dua bot")
        await ctx.channel.send(embed=embed)
    
    @commands.command(name='random')
    @commands.has_permissions(administrator=True)
    async def random(self, ctx):
        await ctx.send(search_image_links(''))
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def bikini(self, ctx):
        await ctx.send(search_image_links("bikini"))

    # We can call the command by its name as an decorator
    # @commands.CommandError()
    # async def dua_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("Oh no, something happened. Please enter the command again.", file=discord.File('bot/img/dua_troste.png'))

async def setup(bot: commands.Bot):
    await bot.add_cog(Dua(bot))