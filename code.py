
import discord
from discord.ext import commands
import requests

r=None
data=None
TOKEN='<your clash royale api token here!!!!>'
header = {"Authorization": f"Bearer {TOKEN}"}
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def s(ctx,tag:str):
    global r,data
    await ctx.send("<:star:1557789692030750780> Fetching data..")
    tag = tag.strip("#").upper()
    r = requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}", headers=header)
    data = r.json()
    embed = discord.Embed(title='<:lp:1557458673259909230> Crownbot',color=0x3498db)
    embed.add_field(name="Player",value=f"{data['name']}\n<:hashtag:1557453324804947998> {data['tag']}\n<:xp:1557449193151397959> {data['expLevel']}\n<:cards:1557451310666752130> {len(data['cards'])}",inline=True)
    embed.add_field(name="Stats",value=f"<:trophy:1557132432593920060> Highest trophies: {data['bestTrophies']}\n<:trophy:1557132432593920060> Current trophies: {data['trophies']}\n<:fight:1557118935088766986> Matches played: {data['battleCount']}\n<:like:1557387163132239902> Wins: {data['wins']}\n<:cry:1557394264898412614> Losses: {data['losses']}\n<:arrow:1557395942733250580> Win rate: {data['wins'] / (data['wins'] + data['losses']) * 100:.2f}%\n<:pol:1557397412983738389> Ranked: {(data.get('currentPathOfLegendSeasonResult') or {}).get('trophies', 'N/A')}\n<:pol:1557397412983738389> Ranked best: {(data.get('bestPathOfLegendSeasonResult') or {}).get('trophies','N/A')}")
    await ctx.send(embed=embed)

@bot.command()
async def h(ctx):
    emb= discord.Embed(title='<:scroll:1557793178109608026> Crownbot Commands')
    emb.add_field(name='!s [tag]',value="View a player's stats.")
    emb.add_field(name='!h', value="View the bot's commands.")
    await ctx.send(embed=emb)

@s.error
async def error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"<:excl:1557797898295451670> You're on cooldown! {error.retry_after:.1f}s.")
    else:
        raise error













        
bot.run("your discord bot token here")