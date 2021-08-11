import discord
from discord.ext import commands
from pytz import timezone, utc

class mods(commands.Cog, name="관리"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="kick", help="상대를 서버 밖으로 내보내는 명령어", aliases=["추방"])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="사유가 지정되지 않음"):
        if member.top_role < ctx.guild.me.top_role:
            try:
                await member.send(f'**{ctx.guild.name}** 서버에서 {reason} 이라는 이유로 {ctx.author}님에게 추방당하셨습니다.')
            except:
                pass
            await ctx.guild.kick(member, reason=reason)
            await ctx.reply(f"**{member}**님을 서버에서 추방하였습니다!\n사유: {reason}")
        else:
            await ctx.reply("제가 추방할려고 하는 유저보다 권한이 낮거나 같아서 추방하지 못했어요!")
            
    @commands.command(name="ban", help="상대를 서버 밖으로 영원히 내쫓는 명령어", aliases=["차단"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="사유가 지정되지 않음"):
        if member.top_role < ctx.guild.me.top_role:
            try:
                await member.send(f'**{ctx.guild.name}** 서버에서 {reason} 이라는 이유로 {ctx.author}님에게 차단당하셨습니다.')
            except:
                pass
            await ctx.guild.ban(member, reason=reason)
            await ctx.reply(f"**{member}**님을 서버에서 차단하였습니다!\n사유: {reason}")
            
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
    bot.add_cog(mods(bot))