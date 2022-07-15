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

        data = requests.get(api)

        lon = data['coord']['lon']
        lat = data['coord']['lat']
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        embed = discord.Embed(title="🌤ㅣ날씨", description="한국 서울 기준으로 날씨를 출력합니다.")
        embed.add_field(name="🌐ㅣ경도 / 위도", value=f"{lon, ', ', lat}", inline=True)
        embed.add_field(name="☀ㅣ날씨", value=f"{weather}", inline=True)
        embed.add_field(name="🌡️ㅣ온도", value=f"{temperature}°C", inline=True)
        embed.add_field(name="🌡️ㅣ습도", value=f"{humidity}", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['서버','서버정보','Guild'])
    async def GuildInfo(self, ctx):
        '''
        Guild Info를 출력합니다.
        '''
        g = ctx.guild
        name = g.name
        afk_voice = g.afk_channel
        banner = g.banner
        system_channel = g.system_channel
        bitrate_limit = g.bitrate_limit
        bitrate_limit = bitrate_limit = str(bitrate_limit)
        bitrate_limit = bitrate_limit.strip("0")
        bitrate_limit = bitrate_limit.strip("000")
        bitrate_limit = bitrate_limit.strip(".")
        emoji_limit = g.emoji_limit 
        filesize_limit = g.filesize_limit
        boost_role = g.premium_subscriber_role
        owner = g.owner
        icon_url = g.icon_url
        is_icon_animated = g.is_icon_animated()
        invite_url_background = g.splash
        member_count = g.member_count
        created_at = g.created_at
        region = g.region
        #invite = await g.invites()

        embed = discord.Embed(title=f"{name}", description=f"{member_count}명의 맴버들과 함께하고 있어요! 이 멋진 봇과 함께요!", color=0xd6ffdb)
        embed.set_thumbnail(url=f"{icon_url}")
        embed.add_field(name="----⚙️일반⚙️----", value="ㅣ모든 서버들이 사용이 가능해요!ㅣ", inline=False)
        embed.add_field(name="🤿ㅣAFK 음성 채널", value=f"{afk_voice}", inline=True)
        embed.add_field(name="🗓ㅣ서버 생성일 UTC", value=f"{created_at}", inline=True)
        embed.add_field(name="🌏ㅣ서버 메인 언어", value=f"{region} (현재 제대로 표시되지 않습니다.)", inline=True)
        embed.add_field(name="📥ㅣ디스코드 관리자 공지 채널", value=f"{system_channel}", inline=True)
        embed.add_field(name="----💎부스트💎----", value="ㅣ부스트일 경우 더 많은 것들이 True로 되어 있어요!ㅣ", inline=False)
        embed.add_field(name="🏷ㅣ부스트 역할", value=f"{boost_role}", inline=True)
        embed.add_field(name="🌌ㅣ서버 아이콘 움직임", value=f"{is_icon_animated}", inline=True)
        embed.add_field(name="🖥ㅣ디스코드 초대 링크 배경화면", value=f"{invite_url_background}", inline=True)
        embed.add_field(name="📃ㅣ서버 배너", value=f"{banner}", inline=True)
        embed.add_field(name="🎤ㅣ서버 비트레이트 한계", value=f"{bitrate_limit}kbps", inline=True)
        embed.add_field(name="😀ㅣ이모지 최대 갯수", value=f"{emoji_limit}개", inline=True)
        embed.add_field(name="🗄ㅣ파일 최대 용량", value=f"{filesize_limit} KIB", inline=True)
        embed.set_footer(text=f"{name}", icon_url=f"{icon_url}")

        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(정보(bot))
