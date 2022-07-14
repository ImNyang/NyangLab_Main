from ast import alias
from re import A
import discord
from discord.ext import commands
import requests

class 정보(commands.Cog):
    '''
    외부 정보를 알려줍니다!
    '''
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['날씨'])
    async def weather(self, ctx):
        city = "Seoul" #도시
        apiKey = "49d31840225c9cca36929d1e2d75b245"
        lang = 'kr' #언어
        units = 'metric' #화씨 온도를 섭씨 온도로 변경
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

        result = requests.get(api)

        lon = result['coord']['lon']
        lat = result['coord']['lat']
        weather = result['weather'][0]['main']
        temperature = result['main']['temp']
        humidity = result['main']['humidity']

        embed = discord.Embed(title="🌤ㅣ날씨", description="한국 서울 기준으로 날씨를 출력합니다.")
        embed.add_field(name="🌐ㅣ경도 / 위도", value=f"{lon, ', ', lat}", inline=True)
        embed.add_field(name="☀ㅣ날씨", value=f"{weather}", inline=True)
        embed.add_field(name="🌡️ㅣ온도", value=f"{temperature}°C", inline=True)
        embed.add_field(name="🌡️ㅣ습도", value=f"{humidity}", inline=True)

def setup(bot):
    bot.add_cog(정보(bot))
