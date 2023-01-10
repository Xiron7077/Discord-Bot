import discord
from discord.ext import commands
import os

def check(id):
  for filename in os.listdir('./cogs'):
    if filename.startswith(f'{id}') and filename.endswith('.txt'):
      return True
      break
    return False

num_warn = 1

class moderation(commands.Cog):
  def __init__(self, rexir):
    self.rexir = rexir
    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator = True)
  async def warn(self, ctx, member : discord.Member, *, reason = None):
    member_id = member.id
    time = ctx.message.created_at
    global num_warn
    embed = discord.Embed(
      title = '',
      description = f"**Reason:** {reason}",
      colour = discord.Colour.green()
    )
    embed.set_author(name = f'{member} has been warned', icon_url = member.avatar_url)

    if not check(member_id):
      new_file = open(f'{member_id}.txt', 'w+')
      new_file.close()
    record = open(f'{member_id}.txt', 'a')
    record.write(f'{num_warn}. {reason}, {time}\n')
    record.close()
    await ctx.send(embed = embed)
    num_warn += 1
    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
  
   if reason == None:
     reason = 'Unspecified'
   try:
     await member.send("""You have been kicked from server
Reason: """+reason)
   except:
     print("Couldn't dm user")
  
   id = member.id
   mod = ctx.author.mention
   channel = self.rexir.get_channel(947617955125006366)
   embed = discord.Embed(
   title = '',
   description = f"""**Reason:**   {reason}
    
**Moderator:** {mod}""",
   colour = discord.Colour.red(),
   timestamp = ctx.message.created_at
  )
   embed.set_author(name = f'{member} has been kicked', icon_url = member.avatar_url)
   embed.set_footer(text = f'ID: {id}')
   await member.kick(reason=reason)
   await channel.send(embed=embed)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
  
   if reason == None:
     reason = 'Unspecified'
   try:
     await member.send("""You have been banned from server
Reason: """+reason)
   except:
     print("Couldn't dm user")
  
   id = member.id
   mod = ctx.author.mention
   channel = self.rexir.get_channel(947617955125006366)
   embed = discord.Embed(
   title = '',
   description = f"""**Reason:**   {reason}
    
**Moderator:** {mod}""",
   colour = discord.Colour.red(),
   timestamp = ctx.message.created_at
  )
   embed.set_author(name = f'{member} has been banned', icon_url = member.avatar_url)
   embed.set_footer(text = f'ID: {id}')
   await member.ban(reason=reason)
   await channel.send(embed=embed)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def unban(self, ctx, user: discord.User):
    embed = discord.Embed(
      title = '',
      description = f"""{user.mention} has been unbanned.
        
Moderator: {ctx.author.mention}""",
      timestamp = ctx.message.created_at,
      colour = discord.Colour.green()
     )
    embed.set_author(name=f'{user}', icon_url=user.avatar_url)
    embed.set_footer(text=f'User ID: {user.id}')
    await ctx.guild.unban(user=user)
    await ctx.send(embed=embed)
    
async def setup(bot):
  await bot.add_cog(moderation(bot))
