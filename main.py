# Dungeons and dragons dice bot for discord
# d20,d12,d10,d6
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print('Bot is online')

@client.command()
async def d20(ctx):
	d20 = random.randint(1,20)
	await ctx.send(d20)

@client.command()
async def d12(ctx):
	d12 = random.randint(1,12)
	await ctx.send(d12)

@client.command()
async def d10(ctx):
	d10 = random.randint(1,10)
	await ctx.send(d10)

@client.command()
async def d6(ctx):
	d6 = random.randint(1, 6)
	await ctx.send(d6)

@client.command()
async def h(ctx):
	await ctx.send("Dice choices name followed by command:")
	await ctx.send("d20 = !d20")
	await ctx.send("d12 = !d12")
	await ctx.send("d10 = !d10")
	await ctx.send("d6 = !d6")
client.run('Discord bot token here')
