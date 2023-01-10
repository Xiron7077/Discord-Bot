import discord
from discord.ext import commands
import os
import tracemalloc
import asyncio
from discord import Intents

intents = Intents.all()
intents.members = True

token = Token
rexir = commands.Bot(command_prefix=">", case_insensitive=True, intents=intents)
rexir.remove_command('help')


def isitme(ctx):
    return ctx.author.id == user


async def load_extensions():
    for file_name in os.listdir("./cogs"):
        if file_name.endswith(".py"):
            await rexir.load_extension(f"cogs.{file_name[:-3]}")


async def main():
    async with rexir:
        await load_extensions()
        await rexir.start(token)


@rexir.event
async def on_ready():
    await rexir.change_presence(activity=discord.Game("Xiron"))


@rexir.command()
@commands.check(isitme)
async def load(ctx, extension):
    await rexir.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension `{extension}` is now loaded')


@rexir.command()
@commands.check(isitme)
async def unload(ctx, extension):
    await rexir.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension `{extension}` is now unloaded')


@rexir.command()
@commands.check(isitme)
async def reload(ctx, extension):
    await rexir.unload_extension(f'cogs.{extension}')
    await rexir.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension `{extension}` is now reloaded')


@rexir.command()
@commands.check(isitme)
async def all_load(ctx):
    for filename_inner in os.listdir('./cogs'):
        if filename_inner.endswith('.py'):
            await rexir.load_extension(f'cogs.{filename_inner[:-3]}')
    await ctx.send(f'All extensions are now loaded')


@rexir.command()
@commands.check(isitme)
async def all_unload(ctx):
    for filename_inner in os.listdir('./cogs'):
        if filename_inner.endswith('.py'):
            await rexir.unload_extension(f'cogs.{filename_inner[:-3]}')
    await ctx.send(f'All extensions are now unloaded')


@rexir.command()
@commands.check(isitme)
async def all_reload(ctx):
    for filename_inner in os.listdir('./cogs'):
        if filename_inner.endswith('.py'):
            await rexir.unload_extension(f'cogs.{filename_inner[:-3]}')
    for filename_inner in os.listdir('./cogs'):
        if filename_inner.endswith('.py'):
            await rexir.load_extension(f'cogs.{filename_inner[:-3]}')
    await ctx.send(f'All extensions are now reloaded')


tracemalloc.start(25)

asyncio.run(main())

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

# pick the biggest memory block
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)
