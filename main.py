import os
import platform
import asyncio

import discord
import config
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!", 
    intents=intents, 
    application_id=config.APP_ID,
    )

@bot.event
async def on_ready() -> None:
    await bot.change_presence(activity=discord.Game(name="Levitating 🚀"))
    print(f"Python version: {platform.python_version()}")
    print(f"Discord API version: {discord.__version__}")
    print("Bot is ready.")

async def load_commands(command_type: str) -> None:
    for file in os.listdir(f'./cogs/{command_type}'):
        if file.endswith('.py'):
            extension = file[:-3]
        try:
            await bot.load_extension(f"cogs.{command_type}.{extension}")
            print(f"Loaded extension '{extension}'")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(f"Failed to load extension {extension}\n{exception}")

async def main():
    await load_commands("normal")
    await bot.start(config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())