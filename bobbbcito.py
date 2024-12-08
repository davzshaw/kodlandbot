import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!k ', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def m1(ctx):
    with open('c5/img/m1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def showImg(ctx):
    listaImg = os.listdir('c5/img')
    await ctx.send(listaImg)
    
    

@bot.command()
async def animal(ctx):
    with open('c5/animal/m1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

from data import TOKEN
bot.run(token=TOKEN)

