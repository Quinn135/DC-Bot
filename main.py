import discord
from dotenv import load_dotenv
from discord.ext import commands
from threading import Thread
from awake import run
import random
from discord_slash import SlashCommand, SlashContext

###############################################################Loading/Variables
load_dotenv()
TOKEN = 'ODg3ODMwNzM4MzkxNjYyNTky.YUJ2zw.k54LH60uCMsF8i80Bl80Rs6xK30'
GUILD = 'donkey club'
bot = discord.Client()
bot = commands.Bot(command_prefix="/")
comm_seperator = ', !'

channel = bot.get_channel(887869955591274538)
##############################################################


#############################################################Ready/Member_Join event
@bot.event
async def on_ready():
    channel = bot.get_channel(887869955591274538)
    embed = discord.Embed(
        title="IM READY!",
        description="I am ready to do the things that I will do!",
        color=discord.Color.blue())
    await channel.send(embed=embed)
    print("ready!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(887869955591274538)
    embed = discord.Embed(title="Welcome " + member.name + "!",
                          description="Welcome to Donkey Club!",
                          color=discord.Color.blue())
    await channel.send(embed=embed)
    print("ready!")


#######################################################################

#@bot.command()
#async def <NAME>(ctx):
#    await ctx.channel.send(<MESSAGE>)



#@bot.command()
#async def NAME(ctx):
#    embed = discord.Embed(title="TITLE", description="DESCRIPTION", color=discord.Color.blue())
#    embed.set_thumbnail(url="THUMBNAIL_URL")
#    await ctx.channel.send(embed=embed)

####################################################################Command
@bot.command()
async def dog(ctx):
    embed = discord.Embed(title="DOGE",
                          description="DOGE ",
                          color=discord.Color.blue())
    embed.set_thumbnail(
        url=
        "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg"
    )
    await ctx.channel.send(embed=embed)


@bot.command()
async def fatman(ctx):
    embed = discord.Embed(title="FATMAN", description="This fat guy cries about his wife. 1 Like and follow = 1 pray!", color=discord.Color.blue())
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Daniel_Lambert_Benjamin_Marshall.jpg/300px-Daniel_Lambert_Benjamin_Marshall.jpg")
    await ctx.channel.send(embed=embed)


@bot.command()
async def thisis1984(ctx):
    embed = discord.Embed(title="1984", description="This is literally 1984.", color=discord.Color.blue())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/887869955591274538/890361276432281670/5fqs99.png")
    await ctx.channel.send(embed=embed)

####################################################
####################################################
memes = ["https://pbs.twimg.com/profile_images/743156951572414472/rzyTdiiR_400x400.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAP5WuTebiw8yKlgS8Yrb4arw5qOb9oOM3_w&usqp=CAU", 'https://cdn.discordapp.com/attachments/887869955591274538/890363179102785546/mzdi5ori22p71.png','https://cdn.memes.com/up/27605031547401535/i/1629692609175.jpg', 'https://cdn.discordapp.com/attachments/887797902540427304/890364149744435240/hpx4htn4v2p71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890364635314782238/967ji6lug0p71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890364775949799484/ix4vffnjl1p71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890365106007990272/7wybeuus42p71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890365487622549504/yes.mp4', 'https://cdn.discordapp.com/attachments/887797902540427304/890365671156903947/00g01u38j3p71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890365873804701716/ppdc466vgzo71.png', 'https://cdn.discordapp.com/attachments/887797902540427304/890366087206690836/oOmK2i2sodExSGPr-yy5I-A-qG3VXY47m2LmTGkuA8U.png']

######################################################

@bot.command()
async def meme(ctx):
    await ctx.channel.send(random.choice(memes))

@bot.command()
async def dchelp(ctx):
    await ctx.channel.send(embed=discord.Embed(title="Help", description="Commands are : /dog, /fatman, /thisis1984,/meme, and /dchelp", color=discord.Color.blue()))
###########################################################################

Thread(target=run).start()
Thread(target=bot.run(TOKEN)).start()
