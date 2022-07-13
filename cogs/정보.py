import discord
from discord.ext import commands
from googletrans import Translator
translator = Translator()


class 정보(commands.Cog):
    '''
    외부 정보를 알려줍니다!
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['서버','서버정보','Guild'])
    async def GuildInfo(self, ctx):
        '''
        Guild Info를 출력합니다.
        '''
        g = ctx.guild
        afk_voice = g.afk_channel
        banner = g.banner_url
        print(afk_voice)
        print(banner)

def setup(bot):
    bot.add_cog(정보(bot))
