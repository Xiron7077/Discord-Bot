import discord
from discord.ext import commands
import main
import asyncio
import random
import math

reco = '<:reco:962826056295915520>'
waiting = "<:waiting_1:960238878940336169>"
weird = '<:sus:960238642998161448>'
dumb = '<:dumb:960238745842503690>'
done = '<:Done:960238795553398834>'
loading = '<a:loading:960238941712302172>'
what = "<:what:962831353987100803>"
come_here = "<:come_here:962831220973121557>"
zero_bet = f"You must be poor, i feel bad, don't {waiting}"
high_bet = f"You dreaming reco now? {weird}"
no_bet = f"What you trying at? {waiting}"
tick = '<:Actioned:959436204519075841>'
cross = '<:Unactioned:959436382114283550>'
duel = "⚔️"
long_sword = ["Long sword", "<:long_sword:959509929847300139>",'ATK', 40,'Spd', 60]
heavy_sword = ["Heavy sword", "<:heavy_sword:959509494382071849>",'ATK', 60,'Spd', 50]
sword = ["Sword", "<:sword:959507301247631380>",'ATK', 30,'Spd', 80]
shield = ["Shield", "<:shield_game:959512751598874624>",'DEF', 50,'Spd', 75]
down_speed = ["Speed spell", "<:spell_book_speed:959514723152433243>",'Rdc', 10,'No', 2]
weapons = (long_sword, heavy_sword, sword, shield, down_speed)

def check(id):
  record = open('record.txt', 'r')
  i = 0
  for check in record:
    check = check.split('-')
    player = check[0]
    value = int(check[1])
    if str(id) == str(player):
      return (True, i, value)
    i += 1
  return (False, i)

def add_coin(id, profit):
  i = check(id)[1]
  value = check(id)[2] + int(profit)
  record_file = open('record.txt', 'r')
  record = record_file.readlines()
  record[i] = f'{id}-{value}\n'
  change = open('record.txt', 'w')
  new_record = "".join(record)
  change.write(new_record)
  record_file.close()
  change.close()

def rem_coin(id, bet):
  i = check(id)[1]
  value = check(id)[2] - int(bet)
  record_file = open('record.txt', 'r')
  record = record_file.readlines()
  record[i] = f'{id}-{value}\n'
  change = open('record.txt', 'w')
  new_record = "".join(record)
  change.write(new_record)
  record_file.close()
  change.close()

class economy(commands.Cog):

  def __init__(self, rexir):
    self.rexir = rexir

  @commands.command()
  @commands.guild_only()
  async def initiate(self, ctx, *, msg=None):
    player_id = ctx.author.id
    if check(player_id)[0]:
      msg = await ctx.send(f"Initaiting account {loading}")
      await asyncio.sleep(2)
      await msg.edit(content = f"Still initiating {loading} {waiting}")
      await asyncio.sleep(2)
      await msg.edit(content = f"Almost there {loading} {waiting}")
      await asyncio.sleep(2)
      await msg.edit(content = f"Human verification failed {weird}")
      await asyncio.sleep(2)
      await ctx.send(f"You are too dumb for a human {dumb}")
      return
    record = open('record.txt', 'a')
    record.write(f'{player_id}-500\n')
    msg = await ctx.send(f"Initiating account {loading}")
    await asyncio.sleep(2)
    await msg.edit(content = f"You have already initiated your account {done}")
    await asyncio.sleep(3)
    await ctx.send(f"You actually fell for it {dumb}")
    await asyncio.sleep(2)
    await ctx.send(f'Your account has been initiated! You currently have **500** {reco}')
    record.close()

  @commands.command()
  @commands.guild_only()
  async def coins(self, ctx, user : discord.Member = None):
    pronoun_1 = "have"
    pronoun_2 = "their"
    user_pronoun = "They"
    target = str(user).split('#')[0]
    if user == None:
      user = ctx.author
      pronoun_1 = "have"
      user_pronoun = "You"
      pronoun_2 = "your"
      if not check(user.id)[0]:
        msg = await ctx.send(f"Checking recos {loading}")
        await asyncio.sleep(2)
        await msg.edit(content = f"You have **100,000** reco {done}")
        await asyncio.sleep(3)
        await ctx.send(f"You actually fell for it {dumb}")
        await asyncio.sleep(2)
        await ctx.send(f'Type >initiate first {waiting}')
        return
    elif not check(user.id)[0]:
      msg = await ctx.send(f"Checking recos {loading}")
      await asyncio.sleep(2)
      await msg.edit(content = f"Verifying their existance {waiting}")
      await asyncio.sleep(2)
      await msg.edit(content = f"They dead mate or he or she or idk anymore {weird}")
      await asyncio.sleep(2)
      await ctx.send(f'You looking for a ghost? {waiting}')
      return
    msg = await ctx.send(f"Checking recos {loading}")
    await asyncio.sleep(2)
    await msg.edit(content = f"{user_pronoun} {pronoun_1}n't initiated {pronoun_2} account {waiting}")
    await asyncio.sleep(2)
    await ctx.send(f"Wait, you actually believed it? {dumb}")
    await asyncio.sleep(2)
    await ctx.send(f"{user_pronoun} {pronoun_1} {check(user.id)[2]} {reco}")
    
  @commands.command()
  @commands.check(main.isitme)
  async def addcoins(self, ctx, user : discord.Member = None, amount = None):
    if user == None:
      user = ctx.author
    if not check(user.id)[0]:
      await ctx.send(f'The player has not initiated their account yet {waiting}')
      return
    target = str(user).split('#')[0]
    add_coin(user.id, int(amount))
    await ctx.send(f"**{amount}** {reco} have been added to {target}'s account!")
  
  @commands.command()
  @commands.guild_only()
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def flip(self, ctx, bet=None, *, choice=None):
    player_id = ctx.author.id
    value = check(player_id)[2]
    options = ['heads','tails']
    choice_check = ['heads', 'head', 'tails', 'tail', 't', 'h']
    if not check(player_id)[0]:
      msg = await ctx.send(f"Flipping reco {loading}")
      await asyncio.sleep(2)
      await msg.edit(f"It's a draw, you won dumbness {dumb}")
      await asyncio.sleep(2)
      await ctx.send(f"Type >initiate first {done}")
      ctx.command.reset_cooldown(ctx)
      return
    elif bet == None:
      await ctx.reply(no_bet)
      ctx.command.reset_cooldown(ctx)
      return
    elif bet in choice_check:
      try:
        bet_1 = bet
        bet = int(choice)
        choice = bet_1
      except:
        ctx.command.reset_cooldown(ctx)
        await ctx.send(f'Enter a valid bet')
        return
    elif not bet in choice_check:
        try:
          test = int(bet)
          if not choice in choice_check:
            ctx.command.reset_cooldown(ctx)
            await ctx.send(f'Enter a valid choice')
            return           
        except:
            ctx.command.reset_cooldown(ctx)
            await ctx.send(f'Enter a valid choice or bet')
            return
    if int(bet) > value:
      await ctx.reply(high_bet)
      ctx.command.reset_cooldown(ctx)
      return
    elif int(bet) == 0:
      await ctx.reply(zero_bet)
      ctx.command.reset_cooldown(ctx)
      return
    elif choice == None:
      choice = random.choice(options)

    choice = choice.lower()
    if choice == "tail":
      choice = "tails"
    elif choice == "head":
      choice = "heads"
    elif choice == 'h':
      choice = "heads"
    elif choice == 't':
      choice = "tails"

    profit = int(bet)*2
    game_choice = random.choice(options)
    player = str(ctx.author).split('#')[0]
    
    await ctx.send(f'{reco} {player} chose {choice}')
    await asyncio.sleep(1)
    resp = await ctx.send(f'{reco} {player} bet **{bet}** ,Flipping coin 5')
    await asyncio.sleep(1)
    await resp.edit(content=f'{reco} {player} bet **{bet}** ,Flipping coin 4')
    await asyncio.sleep(1)
    await resp.edit(content=f'{reco} {player} bet **{bet}** ,Flipping coin 3')
    await asyncio.sleep(1)
    await resp.edit(content=f'{reco} {player} bet **{bet}** ,Flipping coin 2')
    await asyncio.sleep(1)
    await resp.edit(content=f'{reco} {player} bet **{bet}** ,Flipping coin 1')
    await asyncio.sleep(1)
    await resp.edit(content=f"{reco} Flipped coin")
    await asyncio.sleep(1)
    await ctx.send(f"{reco} It's {game_choice}")
    await asyncio.sleep(1)

    if choice == game_choice:
      await ctx.send(f'{reco} {player} won **{profit}** reco')
      add_coin(player_id, bet)
      return
    else:
      await ctx.send(f'{reco} {player} lost **{bet}** reco')
      rem_coin(player_id, bet)
      return

  @commands.command()
  @commands.guild_only()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  async def daily(self, ctx):
    if not check(ctx.author.id)[0]:
      msg = await ctx.send(f"Collecting daily coins {loading}")
      await asyncio.sleep(2)
      await msg.edit(content = f"You claimed your daily **500** {reco}")
      await asyncio.sleep(2)
      await ctx.message(f"Just kidding, you didn't {dumb}")
      await asyncio.sleep(2)
      await ctx.message(f"Type >initiate {waiting}")
      ctx.command.reset_cooldown(ctx)
      return

    add_coin(ctx.author.id, 500)
    msg = await ctx.send(f"Collecting daily coins {loading}")
    await asyncio.sleep(2)
    await msg.edit(content = f"Your coins were eaten by a dragon {weird}")
    await asyncio.sleep(2)
    await ctx.send(f"Wait a sec, the dragon pooped it out {what}")
    await asyncio.sleep(2)
    await ctx.send(f"You claimed your daily **500** {reco} (with poop) {done}")
  
  @commands.command()
  @commands.guild_only()
  @commands.cooldown(1, 3600, commands.BucketType.user)
  async def hourly(self, ctx):
    if not check(ctx.author.id)[0]: 
      msg = await ctx.send(f"Collecting hourly coins {loading}")
      await asyncio.sleep(2)
      await msg.edit(content = f"You claimed your hourly **100** {reco}")
      await asyncio.sleep(2)
      await ctx.message(f"Just kidding, you didn't {dumb}")
      await asyncio.sleep(2)
      await ctx.message(f"Type >initiate {waiting}")
      ctx.command.reset_cooldown(ctx)
      return

    add_coin(ctx.author.id, 500)
    msg = await ctx.send(f"Collecting hourly coins {loading}")
    await asyncio.sleep(2)
    await msg.edit(content = f"A boomer stole it {weird}")
    await asyncio.sleep(2)
    await ctx.send(f"Wait a sec, it was you {what}")
    await asyncio.sleep(2)
    await ctx.send(f"You claimed your daily **500** {reco} (boomer) {done}")

  @commands.command()
  @commands.guild_only()
  @commands.cooldown(1, 120, commands.BucketType.user)
  async def duel(self, ctx, opp : discord.Member = None, bet = None):
    channel = ctx.channel
    player_us = ctx.author
    player = str(player_us).split('#')[0]
    player_id = ctx.author.id
    if opp == None:
      await ctx.reply(f"{duel} No opponent mentioned!")
      ctx.command.reset_cooldown(ctx)
      return
    opponent = str(opp).split('#')[0]
    opponent_id = opp.id
    if not check(player_id)[0]:
      await ctx.reply(f"You haven't initiated your account yet {waiting}, type >initiate to get started {done}")
      ctx.command.reset_cooldown(ctx)
      return
    elif not check(opponent_id)[0]:
      await ctx.reply(f"{duel} Your opponent has not initiated their account yet!")
      ctx.command.reset_cooldown(ctx)
      return
    elif opponent_id == player_id:
      await ctx.reply(f"Damn, how lonely are you? {waiting}")
      ctx.command.reset_cooldown(ctx)
      return
    elif bet == None or bet == None:
      await ctx.reply(no_bet)
      ctx.command.reset_cooldown(ctx)
      return
    elif int(bet) > check(player_id)[2]:
      await ctx.reply(high_bet)
      ctx.command.reset_cooldown(ctx)
      return
    elif int(bet) > check(opponent_id)[2]:
      await ctx.reply(f"Not everyone is that rich {what}")
      ctx.command.reset_cooldown(ctx)
      return

    request = await ctx.send(f"""{opp.mention} you have been challanged to a duel 
**Challanger** : {player_us.mention}
**Bet** : {bet} reco {reco}
React with {tick} to accept or {cross} to decline""")
    await request.add_reaction(tick)
    await request.add_reaction(cross)

    def check_reaction(reaction, user):
      if reaction.message == request and user.id == opponent_id :
        return True

    try:
      r_check = await self.rexir.wait_for('reaction_add', check=check_reaction, timeout=60)
    except asyncio.TimeoutError:
      await request.clear_reaction(tick)
      await request.clear_reaction(cross)
      await request.edit(content = f"{duel} Duel discarded, {opponent} didn't respond in time ")
      ctx.command.reset_cooldown(ctx)
      return
      
    await request.clear_reaction(tick)
    await request.clear_reaction(cross)

    if str(r_check[0]) == cross:
      await request.edit(content = f'{duel} Challange declined {cross}')
      ctx.command.reset_cooldown(ctx)
      return
    elif str(r_check[0]) == tick:
      await request.edit(content = f'{duel} Challange accepted {tick}')

    health1 = 100
    health2 = 100
    for num in range(3):
      await asyncio.sleep(3)
      weapons_list1 = random.sample(weapons, 4)
      weapons_list2 = random.sample(weapons, 4)
      embed = discord.Embed(
        title = "Choose one of the following items",
         colour = discord.Colour.green()
      )
      for i in range(4):
        embed.add_field(name = f"{weapons_list1[i][0]} {weapons_list1[i][1]}", value = f"""{weapons_list1[i][2]} - {weapons_list1[i][3]}
{weapons_list1[i][4]} - {weapons_list1[0][5]}""")
        
      def check_r(reaction, user):
        if reaction.message == dm and user.id == player_id :
          return True
      dm = await player_us.send(embed=embed)

      player1 = player
      
      for i in range(2):
        await dm.add_reaction(weapons_list1[0][1])
        await dm.add_reaction(weapons_list1[1][1])
        await dm.add_reaction(weapons_list1[2][1])
        await dm.add_reaction(weapons_list1[3][1])
        
        wait = await channel.send(f"{duel} {player1} is choosing an item, {opponent} please wait {loading} ")

        try:
          dm_check2 = await self.rexir.wait_for('reaction_add', check=check_r, timeout=30)
        except asyncio.TimeoutError:
          await wait.edit(content = f"{duel} Duel discarded, {player} didn't make a choice in time, Both player's bet has been returned")
          return
        await wait.edit(content = f"{player1} has chosen an item")
        def check_r(reaction, user):
          if reaction.message == dm and user.id == opponent_id :
            return True
        
        if i == 1:
          break

        player1 = opponent
        opponent = player
        dm_check1 = dm_check2
        dm = await opp.send(embed=embed)
      weapon = dm_check1[0]
      for n in range(2):
        for i in range(4):
          if str(weapon) ==  weapons_list1[i][1]:
            if weapons_list1[i][2] == "DEF":
              DEF2 = weapons_list1[i][3]
              Type2 = 'DEF'
            elif weapons_list1[i][2] == "Rdc":
              Rdc2 = weapons_list1[i][3]
              if No2 < weapons_list1[i][5]:
                No2 = weapons_list1[i][5] - 1
              else: 
                No2 = weapons_list1[i][5]
              Type2 = 'Speed reduction'
            else:
              ATK2 = weapons_list1[i][3]
              Type2 = 'ATK'
              
            Spd2 = weapons_list1[i][5]
            weapon2 = weapons_list1[i][0]
            ab_type2 = weapons_list1[i][4]
          
            if n == 1:
              break
            try:
              DEF1 = DEF2
            except:
              pass
            try:
              No1 = No2
            except:
              pass
            try:
              Rdc1 = Rdc2
            except:
              pass
            try:
              ATK1 = ATK2
            except:
              pass
            weapon1 = weapon2
            Spd1 = Spd2
            Type1 = Type2
            ab_type1 = ab_type2

        weapon = dm_check2[0]
        
      await asyncio.sleep(2)

      opponent1 = opponent
      opponent = player1
      player = opponent1
      
      if Spd1 > Spd2:
        if Type1 == "ATK" and Type2 == "ATK":
          health2 = health2 - ATK1
          msg = f"{duel} {player}'s attack landed and reduced {opponent}'s health to **{health2}**"
        elif weapon1 == "Shield":
          ATK1 = DEF1
          health1 = health1 + DEF1 - ATK2
          msg = f"{duel} {player} defended the attack and his health reduced to **{health1}**"
          if health1 >= 100:
            health1 = 100
            msg = f"{duel} {player} defended the attack completely"
        if weapon2 == "Speed spell":
          ATK2 = Spd2
          Spd1 = Spd1 - Rdc2
          No2 = No2 - 1
          msg = f"{duel} {player}'s speed got reduced to **{Spd1}**"
          health1 = 100
        elif weapon2 == "Shield":
          ATK2 = DEF2
          health2 = health2 + DEF2 - ATK1
          msg = f"{duel} {opponent}'s defended the attack and his health reduced to **{health2}**"
          
        await asyncio.sleep(2)
        await channel.send(f"""{duel} {player} chose **{weapon1}**
**{Type1} - {ATK1}**
**{ab_type1} - {Spd1}**""")
        await asyncio.sleep(2)
        await channel.send(f"""{duel} {opponent} chose **{weapon2}**
**{Type2} - {ATK2}**
**{ab_type2} - {Spd2}**""")
        await asyncio.sleep(2)
        await channel.send(msg)
        
        if health1 < 0:
          health1 = 0
        elif health2 < 0:
          health2 = 0
          
      elif Spd2 > Spd1:
        if Type1 == "ATK" and Type2 == "ATK":
          health1 = health1 - ATK2
          msg = f"{duel} {opponent}'s attack landed and reduced {player}'s health to **{health1}**"
        elif weapon2 == "Shield":
          ATK2 = DEF2
          health2 = health2 + DEF2 - ATK1
          msg = f"{duel} {opponent} defended the attack and his health reduced to **{health2}**"
          if health2 >= 100:
            health2 = 100
            msg = f"{duel} {opponent} defended the attack completely"
        if weapon1 == "Speed spell":
          ATK1 = Spd1
          No1 = No1 - 1
          Spd2 = Spd2 - Rdc1
          msg = f"{duel} {opponent}'s speed got reduced to **{Spd2}**"
          health2 = 100
        elif weapon1 == "Shield":
          ATK1 = DEF1
          health1 = health1 + DEF1 - ATK2
          msg = f"{duel} {player}'s defended the attack and his health reduced to **{health1}**"

        await asyncio.sleep(2)
        await channel.send(f"""{duel} {opponent} chose **{weapon2}**
**{Type2} - {ATK2}**
**{ab_type2} - {Spd2}**""")
        await asyncio.sleep(2)
        await channel.send(f"""{duel} {player} chose **{weapon1}**
**{Type1} - {ATK1}**
**{ab_type1} - {Spd1}**""")
        await asyncio.sleep(1)
        await channel.send(msg)

        if health1 < 0:
          health1 = 0
        elif health2 < 0:
          health2 = 0
        
      elif Spd1 == Spd2:
        if Type1 == "DEF":
          msg = f"Nothing happened, you both scared {waiting}"
        elif Type1 == "ATK":
          health1 = health1 - ATK2
          health2 = health2 - ATK1
          msg = f"""{duel} Both player's attack landed
{duel} Both player's health reduced to **{health1}**"""
        elif Type1 == "Speed reduction":
          Spd1 = Spd1 - Rdc2
          Spd2 = Spd2 - Rdc1
          msg = f"""{duel} Both player's speed reduced by **{Spd1}**"""
        
        await asyncio.sleep(2)
        await channel.send(f"""{duel} Both players chose **{weapon1}** 
**{Type1} - {ATK1}** 
**{ab_type1} - {Spd1}**""")
        await asyncio.sleep(2)
        await ctx.send(msg)

        if health1 < 0:
          health1 = 0
        elif health2 < 0:
          health2 = 0

      profit = bet*2
      
      if num >= 1:
        if health1 == 0:
          add_coin(opponent_id, profit)
          await ctx.send(f"{player} lost the duel")
          await ctx.send(f"{opponent} won and got {profit}")
        elif health2 == 0:
          add_coin(player_id ,profit)
          await ctx.send(f"{opponent} lost the duel")
          await ctx.send(f"{player} won and got {profit}")
        elif health1 == 0 and health2 == 0:
          await ctx.send(f"Both players lost all their health, it's a draw")
      if num == 2:
        if health1 > health2:
          add_coin(player_id ,profit)
          await ctx.send(f"{player} won the duel and got {profit} {reco}")
          await ctx.send(f"{opponent} lost the duel and {bet} {reco}")
        elif health2 > health1:
          add_coin(opponent_id, profit)
          await ctx.send(f"{opponent} won the duel and got {profit} {reco}")
          await ctx.send(f"{player} lost the duel and {bet} {reco}")
        else:
          await ctx.send(f"It's a draw, bets returned")

  @commands.command()
  @commands.guild_only()
  async def test(self, ctx, *, msg=None):
    await ctx.send(f'{sword[1]}   {sword[1]}')
  
  @flip.error
  async def flip_error(self, ctx, error):
    seconds = round(error.retry_after)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f"**You can use flip again after {seconds} seconds**")

  @hourly.error
  async def hourly_error(self, ctx, error):
    minutes = round(round(error.retry_after)/60)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f"**You can claim your hourly again after {minutes} minutes**")

  @daily.error
  async def daily_error(self, ctx, error):
    hours_deci = round(round(error.retry_after)/60)/60
    hours = math.floor(hours_deci)
    minutes = round((int(str(math.floor(hours_deci*100)/100).split('.')[1])*60)/100)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f"**You can claim your daily after {hours} hours and {minutes} minutes**")
 
  @duel.error
  async def duel_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      ra = error.retry_after
      minutes = round(round(ra)/60)
      await ctx.reply(f"**You can duel again after {minutes} minutes**")
      
def setup(bot):
  bot.add_cog(economy(bot))
