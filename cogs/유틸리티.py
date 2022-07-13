import discord
from discord.ext import commands


class 유틸리티(commands.Cog):
    '''
    봇의 대한 정보나 유용한 커맨드들을 정리했습니다.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['핑', 'pong', '퐁'], pass_context=True)
    async def ping(self, ctx):
        '''이 봇과 디스코드 서버까지 왕복한 시간을 출력합니다.''' #불1편
        embed = discord.Embed(title="🏓ㅣPong", description=f"`{round(round(self.bot.latency, 4)*1000)}ms`", color=0xff0000)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['서버입장'], pass_context=True)
    async def joined(self, ctx, member: discord.Member):
        """핑한 사람이 얼마나 오래 이 서버에 있었는지 알 수 있습니다."""
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

def setup(bot):
    bot.add_cog(유틸리티(bot))
