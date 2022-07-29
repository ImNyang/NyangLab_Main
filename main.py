import discord
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp
import os
import datetime
import jishaku
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
from random import randint

# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.
menu = DefaultMenu(page_left="⬅️", page_right="➡️", remove="❌", active_time=30)

# Custom ending note
ending_note = "{ctx.bot.user.name}의 설명서 \n{help.clean_prefix}{help.invoked_with}으로 도움말을 알 수 있어요!"

bot = commands.Bot(command_prefix='..')
bot.load_extension('jishaku')
bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)

url = str(os.getenv('PINGPONG_URL'))  # 핑퐁빌더 Custom API URL
pingpong_token = str(os.getenv('PINGPONG_TOKEN'))  # 핑퐁빌더 Custom API Token

Ping = PingPong(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    user = await bot.fetch_user("909353223901569035")
    await user.send("✅ㅣ봇이 준비되었습니다!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="냥 도움말"))

@bot.event
async def on_member_update():
    n = 535432063042715649
    await n.edit(nick="메이드 뇽룡")

badwords = ['discord.gg', 'discord.com/invites', 'https://aztra.xyz/invite/', 'youtube.com/c/']

@bot.event
async def on_message(message):
    if message.author == bot.user: # 만약 메시지를 보낸 사람과 봇이 서로 같을 때
        return

    elif message.author.bot: # discord.User.bot 프로퍼티가 참일 때
        return
    for i in badwords: # Go through the list of bad words;
      if i in message.content:
         await message.delete()
         embed = discord.Embed(title=f"죄송합니다.", description="이 서버에선 아직 홍보방이 없으며 \n디스코드 초대링크나 보안 초대링크는 사용이 불가능 합니다.\n 유튜브도 불가능하죠! 하지만 유저들의 편의를 위해 유튜브 링크는 가능하지만 \n홍보 용도는 알아서 차단하겠습니다.")
         embed.set_footer(text="반복적으로 한다면 타임아웃이 적용될 수 있습니다.")
         await message.channel.send(f"{message.author.mention}",embed=embed)
         channel = bot.get_channel(993065739865038918)
         embedlog = discord.Embed(title="디스코드 초대 링크 감지!", description=f"{message.author.mention}\n {message}", color=0xff0000)
         embedlog.timestamp = datetime.datetime.now()
         await channel.send(embed=embedlog)
         bot.dispatch('profanity', message, i)
         return # So that it doesn't try to delete the message again, which will cause an error.
    await bot.process_commands(message)

def RandomColor():
    return randint(0, 0xFFFFFF)
@bot.listen()
async def on_command_error(ctx, error):
    if type(error) is commands.errors.CommandNotFound:
        data = await Ping.Pong(ctx.author.id, ctx.message.content, NoTopic=False)
        embed = discord.Embed(
            title="PingPong.us로 나온 결과!",
            description=data['text'],
            color=RandomColor()
        )
        embed.set_footer(text="Using PingPongTool")
        if data['image'] is not None:
            embed.set_image(url=data['image'])
        await ctx.send(embed=embed)

bot.run(str(os.getenv('TOKEN')))