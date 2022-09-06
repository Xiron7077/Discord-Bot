import discord
from discord.ext import commands
import main
import asyncio

class command(commands.Cog):

  def __init__(self, rexir):
    self.rexir = rexir

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is up and going')

  @commands.command()
  @commands.guild_only()
  async def ping(self, ctx):
    await ctx.send(f'Pong! `{round(self.rexir.latency*1000)}ms`')
    
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def dm(self, ctx, member : discord.Member, *, msg=None):
    await member.send(msg)
    await ctx.send('Member has been dmed.')
    await ctx.message.delete()

def setup(bot):
  bot.add_cog(command(bot))