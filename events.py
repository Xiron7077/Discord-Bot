import discord
from discord.ext import commands
import main

class event(commands.Cog):

  def __init__(self, rexir):
    self.rexir = rexir

  @commands.Cog.listener()
  async def on_message(self, message):
   username = str(message.author).split('#')[0]
   triggersofhey = ['hey rexir', 'heya rexir', 'hello rexir', 'sup rexir', 'hi rexir', 'rexir :wave:']
   if message.content.lower() in triggersofhey:
     await message.channel.send(f'Hey there {username}!')

def setup(bot):
  bot.add_cog(event(bot))