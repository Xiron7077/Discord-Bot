import discord
from discord.ext import commands
import os
from discord import Intents
import random
import time
import asyncio
from math import *

intents = Intents.default()
intents.members = True

token = os.environ['Token']
rexir = commands.Bot(command_prefix = ">", case_insensitive=True, intents=intents)
rexir.remove_command('help')


def isitme(ctx):
  return ctx.author.id == User

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    rexir.load_extension(f'cogs.{filename[:-3]}')


@rexir.event
async def on_ready():
 await rexir.change_presence(activity=discord.Game("Xiron"))


@rexir.command()
@commands.check(isitme)
async def load(ctx, extension):
  rexir.load_extension(f'cogs.{extension}')
  await ctx.send(f'The extension `{extension}` is now loaded')

@rexir.command()
@commands.check(isitme)
async def unload(ctx, extension):
  rexir.unload_extension(f'cogs.{extension}')
  await ctx.send(f'The extension `{extension}` is now unloaded')

@rexir.command()
@commands.check(isitme)
async def reload(ctx, extension):
  rexir.unload_extension(f'cogs.{extension}')
  rexir.load_extension(f'cogs.{extension}')
  await ctx.send(f'The extension `{extension}` is now reloaded')

@rexir.command()
@commands.check(isitme)
async def alload(ctx):
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      rexir.load_extension(f'cogs.{filename[:-3]}')
  await ctx.send(f'All extensions are now loaded')
  
@rexir.command()
@commands.check(isitme)
async def uload(ctx):
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      rexir.unload_extension(f'cogs.{filename[:-3]}')
  await ctx.send(f'All extensions are now unloaded')
    
@rexir.command()
@commands.check(isitme)
async def reloadall(ctx):
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      rexir.unload_extension(f'cogs.{filename[:-3]}')
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      rexir.load_extension(f'cogs.{filename[:-3]}')
  await ctx.send(f'All extensions are now reloaded')

rexir.run(token)
