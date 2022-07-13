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

    @commands.command()
    async def Translaton(self,ctx,lang:str,text:str):
        '''
        번역을 합니다.
        '''
        if lang == "zh-cn" or lang == "중국어_간체":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='zh-cn')}")
            await ctx.reply(embed=embed)
        elif lang == "zh-tw" or lang == "중국어 번체":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='zh-tw')}")
            await ctx.reply(embed=embed)
        elif lang == "en" or lang == "영어":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='en')}")
            await ctx.reply(embed=embed)
        elif lang == "fr" or lang == "프랑스어":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='fr')}")
            await ctx.reply(embed=embed)
        elif lang == "ja" or lang == "일본어":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='ja')}")
            await ctx.reply(embed=embed)
        elif lang == "ko" or lang == "한국어":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='ko')}")
            await ctx.reply(embed=embed)
        elif lang == "uk" or lang == "우크라이나어":
            embed = discord.Embed(title=f"Translaton {lang}", description=f"{translator.translate(text, dest='uk')}")
            await ctx.reply(embed=embed)
        else:
            await ctx.reply('지원하는 언어로 해주세요!', file=discord.File("translaton_lang.json"))

def setup(bot):
    bot.add_cog(정보(bot))
