import asyncio
import os
import discord
import config
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, application_id=config.APP_ID)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Levitating", url="https://www.youtube.com/watch?v=TUVcZfQe-Kw"))
    print("Bot is ready.")

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())