import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

##Loading/Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()
bot = commands.Bot(command_prefix="!")
points = 0
comm_seperator = ', !'

commands = ['dog']
###################


##Ready event
@bot.event
async def on_ready():
    channel = bot.get_channel(667112912774758472)
    await channel.send(
        'Im ready to haunt your dreams forever! **evil laugh** Also, right now, the commands are : !'
        + comm_seperator.join(commands))
    print("ready! " + comm_seperator.join(commands))


#############

#@bot.command()
#async def <NAME>(ctx):
#    await ctx.channel.send(<MESSAGE>)


##Command
@bot.command()
async def dog(ctx):
    await ctx.channel.send(
        "Hi, I see you said dog! If you have any ideas for features, please dm QuinnC. Thanks!"
    )

bot.run(TOKEN)