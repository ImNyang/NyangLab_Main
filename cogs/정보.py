import discord
from discord.ext import commands


class 정보(commands.Cog):
    '''
    외부 정보를 알려줍니다!
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['IT', 'event', '이벤트'], pass_context=True)
    async def ITevent(self, ctx, what:str = "None"):
        """IT Event를 알 수 있습니다. (수동 등록)"""
        if what == "Nothing":
            embed = discord.Embed(title="🎪ㅣNothing Event on", description="<t:1657638000:f> KST", url="https://youtu.be/XDcl6CYY7-A")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="알 수 없는 전자기기 이벤트", description="현재 있는 이벤트")
            embed.add_field(name="`Nothing`", value="`Nothing Event`", inline=False)
            await ctx.reply(embed=embed)
    

def setup(bot):
    bot.add_cog(정보(bot))
