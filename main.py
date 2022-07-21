import discord
from discord.ext import commands
import os
import datetime
import jishaku
import PingPongWr, random

# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.

# Custom ending note
ending_note = "{ctx.bot.user.name}의 설명서 \n{help.clean_prefix}{help.invoked_with}으로 도움말을 알 수 있어요!"

bot = commands.Bot(command_prefix='..')
bot.load_extension('jishaku')

url = str(os.getenv('PINGPONG_URL'))  # 핑퐁빌더 Custom API URL
pingpong_token = str(os.getenv('PINGPONG_TOKEN'))  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

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
async def on_command_error(ctx, error):
    embed=discord.Embed(title="Error!", description="어... 이게 무슨 상황인지 개발자에게 알려주세요!")
    embed.add_field(name="오류 내용", value=f"`{str(error)}`", inline=True)
    embed.set_footer(text="Dm : ImNyang#9009")
    await ctx.send(embed=embed)

badwords = ['discord.gg', 'discord.com/invites', 'https://aztra.xyz/invite/']

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

@bot.command(aliases=["대화"])
async def chat(ctx, chat:str):
    str_text = (chat.split(" "))[1]
    return_data = await Ping.Pong(session_id ="Example", text = str_text, topic = True, image = True, dialog = True) # 핑퐁빌더 API에 Post 요청
    await ctx.reply(str(return_data["text"]))

@bot.slash_command(guild_ids=[993042304325664791])
async def 안녕(ctx):
    await ctx.respond(f"Hello! World! `Pong! {round(round(bot.latency, 4)*1000)}ms`")

@bot.slash_command()
async def 가위바위보(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)  # 인덱스 비교로 결과 결정
    if result == 0:
        await ctx.respond(f'{user} vs {bot}  비겼습니다.')
    elif result == 1 or result == -2:
        await ctx.respond(f'{user} vs {bot}  유저가 이겼습니다.')
    else:
        await ctx.respond(f'{user} vs {bot}  봇이 이겼습니다.')

bot.run(str(os.getenv('TOKEN')))
