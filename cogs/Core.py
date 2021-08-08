import discord
from discord.ext import commands

class Core(commands.Cog, name="일반"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="핑", help="봇의 속도와 클라이언트 핑을 알려줘요!", aliases=["ping"])
    async def ping(self, ctx):
        embed1 = discord.Embed(title='핑 측정 결과', description='다음은 민트초코 봇의 핑 측정 결과 입니다!')
        embed1.add_field(name="API 핑(ms)", value=str(round(self.bot.latency * 1000)))
        embed1.set_thumbnail(url=ctx.author.avatar_url_as(static_format="png", size=2048))
        await ctx.reply(content=None, embed=embed1)

    @commands.command(name="개발자", help="민트초코 봇의 개발자를 알려줘요!", aliases=["hellothisisverification"])
    async def hellothisisverification(self, ctx):
        await ctx.reply(f'저를 만들어 주신 분은\n정희인데 _#1063 님\n수박#3754 님\n아이스크림 해피#5764 님\nMisile#1231 님 입니다!')

    @commands.command(name="초대", help="민트초코 봇의 초대링크를 보내줘요!", aliases=["invite"])
    async def invite(self, ctx):
        embed = discord.Embed(title='**민트초코 봇 초대하기!**',
                              description='저를 초대하고 싶으신가요?\n**[여기](https://discord.com/api/oauth2/authorize?client_id=864683154647810089&permissions=8&scope=bot)**를 클릭해서 초대해 보세요!',
                              colour=0x98FB98)

        await ctx.send(embed=embed)

    @commands.command(name="청소", help="드러워진 채팅방을 청소해줘요!", aliases=["clear", "clean"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.channel)
    async def clear(self, ctx, num: int):
        if num <= 100 and num > 0:
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=num)
            await ctx.send(
                f":sponge: {ctx.author.mention} {len(deleted)}개의 메세지를 삭제했어요!\n \n이 메시지는 5초뒤에 삭제됩니다!",
                delete_after=5,
            )

def setup(bot):
    bot.add_cog(Core(bot))