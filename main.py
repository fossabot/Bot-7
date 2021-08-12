import discord
import os
from discord.ext import commands
import discord.ext.tasks
from jishaku.cog import Jishaku

owners = [673471748599054336, 338902243476635650]
TOKEN = "ODc1MjAxMTkwNzA1NjU5OTU1.YRSEoA.eyja6lXmm-2Ci7F7eg-goAO8OQk"

bot = commands.Bot(command_prefix='=', owner_ids = set(owners), intents=discord.Intents.all())

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"cogs.{file[:-3]} - 로드 성공!")

bot.load_extension('jishaku')

@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Watson', url="https://twitch.tv/jeongheegenius"))

bot.run(TOKEN)