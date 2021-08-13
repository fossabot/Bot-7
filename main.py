import discord
import os
from discord.ext import commands
import discord.ext.tasks
from jishaku.cog import Jishaku
import dotenv
from dotenv import *

owners = [673471748599054336, 338902243476635650]

config = dotenv_values(".env")
token = config["token"]

bot = commands.Bot(command_prefix='민초야 ', owner_ids = set(owners), intents=discord.Intents.all())

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"cogs.{file[:-3]} - 로드 성공!")

bot.load_extension('jishaku')

@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'{bot.command_prefix} help를 입력해 보아요!'))

bot.run(token)