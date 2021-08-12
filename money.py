import discord
from discord.ext import commands

class money(commands.Cog, name="돈"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="지갑", help="나의 지갑을 확인하는 명령어")
    async def wallet(self, ctx):
    
def setup(bot):
    bot.add_cog(money(bot))