import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.idle, activity=discord.Game('My prefix is >'))
     print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")


client.run("Token here")
