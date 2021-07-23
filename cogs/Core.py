import discord
from discord.ext import commands

class Core(commands.Cog, name="일반"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="핑", help="봇의 속도와 클라이언트 핑을 알려줘요!", aliases=["ping"])
    async def ping(self, ctx):
        await ctx.reply(f'퐁! - {round(self.bot.latency * 1000)}ms')

    @commands.command(name="개발자", help="민트초코 봇의 개발자를 알려줘요!", aliases=["hellothisisverification"])
    async def hellothisisverification(self, ctx):
        await ctx.reply(f'저를 만들어 주신 분은\n정희인데 _#1063 님\n수박#3754 님\n아이스크림 해피#5764 님\nMisile#1231 님 입니다!')


def setup(bot):
    bot.add_cog(Core(bot))