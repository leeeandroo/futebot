import discord
import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def roll(ctx, arg):
    try:
        rolled = random.randrange(1, int(arg))
        await ctx.send('Rolled ' + str(rolled))
    except:
        await ctx.send('Are you dumb?')

bot.run(os.environ['DISCORD_APP_TOKEN'])
