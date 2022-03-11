import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

@bot.command()
async def repeter(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def repeterDeux(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))

@bot.command()
async def repeterMultiple(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

bot.run(TOKEN)


