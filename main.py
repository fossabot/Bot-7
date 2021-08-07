import discord, os
from discord.ext import commands
import discord.ext.tasks
from jishaku.cog import Jishaku

owners = [673471748599054336, 338902243476635650, 551212082645827594, 694545037014597664, 694027673088819210]

bot = commands.Bot(command_prefix='민초야 ', owner_ids = set(owners), intents=discord.Intents.all())
TOKEN = "ODY0NjgzMTU0NjQ3ODEwMDg5.YO5A8Q._EOhOu7XhK2fKJvEtk4YsG45JUA"

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"cogs.{file[:-3]} - 로드 성공!")

bot.load_extension('jishaku')

@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'{bot.command_prefix} help를 입력해 보아요!'))

bot.run(TOKEN)