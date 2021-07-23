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

    @commands.command(name="초대", help="민트초코 봇의 초대링크를 보내줘요!", aliases=["invite"])
    async def invite(self, ctx):
        embed = discord.Embed(title='**민트초코 봇 초대하기!**',
                              description='저를 초대하고 싶으신가요?\n**[여기](https://discord.com/api/oauth2/authorize?client_id=864683154647810089&permissions=8&scope=bot)**를 클릭해서 초대해 보세요!',
                              colour=0x98FB98)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Core(bot))