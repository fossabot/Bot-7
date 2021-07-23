import discord, asyncio, os
from discord.ext import commands
from jishaku.cog import Jishaku

bot = commands.Bot(command_prefix='민초야 ', intents=discord.Intents.all())
TOKEN = "ODY0NjgzMTU0NjQ3ODEwMDg5.YO5A8Q._EOhOu7XhK2fKJvEtk4YsG45JUA"

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"cogs.{file[:-3]} - 로드 성공!")

bot.load_extension('jishaku')

bot.help_command=None

@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비완료!")

bot.run(TOKEN)