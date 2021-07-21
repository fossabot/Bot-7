import discord
from discord.ext import commands

class Core(commands.Cog, name="일반"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="핑", help="봇의 속도와 클라이언트 핑을 알려줘요!", aliases=["ping"])
    async def ping(self, ctx):
        await ctx.reply("퐁!")

def setup(bot):
    bot.add_cog(Core(bot))