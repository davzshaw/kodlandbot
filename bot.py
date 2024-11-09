import discord
from discord.ext import commands
from botlogic import generatePassword
from datetime import datetime

t = "MTMwMjA3NDQzNTA1ODI3NDQ2Nw.GzBwli.8824oE8GLAxn9w0Pl-HVSqQQeWKyBLYBROgX24"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!kodlandbot ', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def password(ctx, passwordLenght):
    passwordLenght = int(passwordLenght)
    await ctx.send(generatePassword(passwordLenght))

bot.run(t)
