import discord
from discord.ext import commands

class money(commands.Cog, name="돈"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="", help="", aliases=[""])
    
def setup(bot):
    bot.add_cog(money(bot))