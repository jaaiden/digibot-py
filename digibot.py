import discord
from discord.ext import commands

memes = commands.Bot(command_prefix='!')

@memes.event
async def on_ready():
    await memes.change_presence(activity=discord.Game(name="absolutely nothing"))

@memes.command()
async def nothing(ctx):
    pass
    
memes.run(token)
