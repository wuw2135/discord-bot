import discord
from discord.ext import commands
import random


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot以上線!")

@bot.event
async def on_member_join(member):                
    #成員加進來的時候跳出訊息
    channel = bot.get_channel(565933724517138465)
    await channel.send(f'{member}加進來了(ﾉ>ω<)ﾉ')

@bot.event
async def on_member_remove(member):              
    #成員離開的時候跳出訊息     
    channel = bot.get_channel(565933724517138465)
    await channel.send(f'{member}走掉了｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡')

@bot.command()
async def cat(ctx):
    random_gif = random.choice(['https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif',
    'https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif',
    'https://media.giphy.com/media/DUO76cKAFAObu/giphy.gif'])
    await ctx.send(random_gif)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1008)} (ms)')

@bot.command()
async def morecat(ctx):
    embed=discord.Embed(title="GIPHY/CAT", url="https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif", description="貓咪GIF", color=0xa74fff)
    embed.set_author(name="CAT", url="https://giphy.com/explore/cat", icon_url="https://media.giphy.com/media/xTiQygY6HW1GjoYKFq/giphy.gif")
    embed.set_thumbnail(url="https://media.giphy.com/media/JoDT2WaykzFnN9vJqL/giphy.gif")
    embed.set_image(url="https://media.giphy.com/media/xTiQygY6HW1GjoYKFq/giphy.gif")
    embed.add_field(name="更多", value="https://media.giphy.com/media/RhrAmVUHxjTQvEPBWi/giphy.gif", inline=False)
    embed.add_field(name="更多", value="https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif", inline=True)
    embed.add_field(name="還有更多", value="https://media.giphy.com/media/l6Td5sKDNmDGU/giphy.gif", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 天竺鼠車車(ctx):
    pic = 'https://i.imgur.com/vYqI6N0.jpg'
    await ctx.send(pic)

@bot.event
async def on_message(msg):
    if msg.content.endswith('梗圖'):
        random_pic=random.choice(['https://i1.kknews.cc/SIG=2qnkltm/ctp-vzntr/2519ooo1n71s436qn7223rq700rso844.jpg',
                                  'https://truth.bahamut.com.tw/s01/201801/f7af15b7de6c27b35e4eed204f22f5e9.JPG?w=1000',
                                  'https://truth.bahamut.com.tw/s01/201801/4e892d01e6c423b3e7918f49d51a0045.JPG?w=1000'])
        await msg.channel.send(random_pic)
    await bot.process_commands(msg)

bot.run('ODA2NTc1OTExMDMzNTAzNzk1.YBrcWg.uWD0l_9CsyHE2FGmYcIcPUbRIH0')
