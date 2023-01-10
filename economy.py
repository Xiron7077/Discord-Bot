import discord
from discord.ext import commands
import asyncio
import random
import json

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


def isitme(ctx):
    return ctx.author.id == user


def check(player_id):
    with open('record.json') as f:
        data = json.load(f)
        i = 0
        for record in data["Record"]:
            if record["id"] == str(player_id):
                return True, i, record["coins"]
            i += 1
    return False, i


def add_coin(player_id, profit):
    i = check(player_id)[1]
    value = check(player_id)[2] + int(profit)
    with open("record.json") as f:
        data = json.load(f)
    with open("record.json", "w") as f:
        data["Record"][i]["coins"] = value
        json.dump(data, f, indent = 2)


def rem_coin(player_id, bet):
    i = check(player_id)[1]
    value = check(player_id)[2] - int(bet)
    with open("record.json") as f:
        data = json.load(f)
    with open("record.json", "w") as f:
        data["Record"][i]["coins"] = value
        json.dump(data, f, indent = 2)


def time_check(player_id, game, time):
    i = check(player_id)[1]
    year = int(time.split("-")[0])
    month = int(time.split("-")[1])
    date = int(time.split("-")[2].split(" ")[0])
    hours = int(time.split(" ")[1].split(":")[0])
    minutes = int(time.split(" ")[1].split(":")[1])
    seconds = float(time.split(" ")[1].split(":")[2].split(':')[0].split('+')[0])
    with open("record.json") as f:
        data = json.load(f)
    if data["Record"][i][game] == 0:
        with open("record.json", "w") as f:
            data["Record"][i][game] = time
            json.dump(data, f, indent = 2)
        return
    time_before = data["Record"][i][game]
    year_before = int(time_before.split("-")[0])
    month_before = int(time_before.split("-")[1])
    date_before = int(time_before.split('-')[2].split(" ")[0])
    hours_before = int(time_before.split(' ')[1].split(':')[0])
    minutes_before = int(time_before.split(' ')[1].split(':')[1])
    seconds_before = float(time_before.split(" ")[1].split(":")[2].split(':')[0].split('+')[0])

    return year_before, year, month_before, month, date_before, date, hours_before, hours, minutes_before, minutes, seconds_before, seconds


def time_add(player_id, game, time):
    i = check(player_id)[1]
    with open("record.json") as f:
        data = json.load(f)
    with open("record.json", "w") as f:
        data["Record"][i][game] = time
        json.dump(data, f, indent = 2)


class Economy(commands.Cog):

    def __init__(self, rexir):
        self.rexir = rexir

    @commands.command()
    @commands.guild_only()
    async def initiate(self, ctx, *, msg=None):
        player_id = ctx.author.id
        if check(player_id)[0]:
            msg = await ctx.send(f"Initiating account {loading}")
            await asyncio.sleep(2)
            await msg.edit(content = f"Still initiating {loading} {waiting}")
            await asyncio.sleep(2)
            await msg.edit(content = f"Almost there {loading} {waiting}")
            await asyncio.sleep(2)
            await msg.edit(content = f"Human verification failed {weird}")
            await asyncio.sleep(2)
            await ctx.send(f"You are too dumb for a human {dumb}")
            return
        with open("record.json") as f:
            data = json.load(f)
        player_id = str(player_id)
        data["Record"].append({"id": player_id, "coins": 500, "loss": 0, "gain": 0, "worth": 0})
        with open("record.json", "w") as f:
            json.dump(data, f, indent = 2)
        msg = await ctx.send(f"Initiating account {loading}")
        await asyncio.sleep(2)
        await msg.edit(content = f"You have already initiated your account {done}")
        await asyncio.sleep(3)
        await ctx.send(f"You actually fell for it {dumb}")
        await asyncio.sleep(2)
        await ctx.send(f'Your account has been initiated! You currently have **500** {reco}')

    @commands.command()
    @commands.guild_only()
    async def coins(self, ctx, user : discord.Member = None):
        pronoun_1 = "have"
        pronoun_2 = "their"
        user_pronoun = "They"
        user_name = str(user).split('#')[0]
        if user is None:
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
            await msg.edit(content = f"Verifying their existence {waiting}")
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
    @commands.check(isitme)
    async def add_coins(self, ctx, user : discord.Member = None, amount = None):
        if user is None:
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
        options = ['heads','tails']
        choice_check = ['heads', 'head', 'tails', 'tail', 't', 'h']
        if not check(player_id)[0]:
            msg = await ctx.send(f"Flipping reco {loading}")
            await asyncio.sleep(2)
            await msg.edit(content = f"It's a draw, you won dumbness {dumb}")
            await asyncio.sleep(2)
            await ctx.send(f"Type >initiate first {done}")
            ctx.command.reset_cooldown(ctx)
            return
        value = check(player_id)[2]
        if bet is None:
            await ctx.reply(no_bet)
            ctx.command.reset_cooldown(ctx)
            return
        elif choice is None:
            choice = random.choice(options)
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

        check_val = True
        time = str(ctx.message.created_at)
        comp = time_check(ctx.author.id, "daily", time)
        if comp[0] > comp[1] or comp[2] > comp[3]:
            check_val = True
        elif comp[4] + 1 > comp[5]:
            check_val = False
        elif comp[4] + 1 == comp[5]:
            if comp[6] > comp[7]:
                check_val = False
            elif comp[8] > comp[9]:
                check_val = False
            elif comp[8] == comp[9] and comp[10] > comp[11]:
                check_val = False
        if not check_val:
            await ctx.reply(f"**You can claim your daily after hour and minutes**")
            return

        add_coin(ctx.author.id, 1000)
        msg = await ctx.send(f"Collecting daily coins {loading}")
        await asyncio.sleep(2)
        await msg.edit(content = f"Your coins were eaten by a dragon {weird}")
        await asyncio.sleep(2)
        await ctx.send(f"Wait a sec, the dragon pooped it out {what}")
        await asyncio.sleep(2)
        await ctx.send(f"You claimed your daily **500** {reco} (with poop) {done}")
        time_add(ctx.author.id, "daily", time)

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
        if opp is None:
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
        elif bet is None or bet == 0:
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

        request = await ctx.send(f"""{opp.mention} you have been challenged to a duel 
    **Challenger** : {player_us.mention}
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
            await request.edit(content = f'{duel} Challenge declined {cross}')
            ctx.command.reset_cooldown(ctx)
            return
        elif str(r_check[0]) == tick:
            await request.edit(content = f'{duel} Challenge accepted {tick}')

        health_1 = 100
        health_2 = 100
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

            player_1 = player

            for i in range(2):
                await dm.add_reaction(weapons_list1[0][1])
                await dm.add_reaction(weapons_list1[1][1])
                await dm.add_reaction(weapons_list1[2][1])
                await dm.add_reaction(weapons_list1[3][1])

                wait = await channel.send(f"{duel} {player_1} is choosing an item, {opponent} please wait {loading} ")

                try:
                    dm_check2 = await self.rexir.wait_for('reaction_add', check=check_r, timeout=30)
                except asyncio.TimeoutError:
                    await wait.edit(content = f"{duel} Duel discarded, {player} didn't make a choice in time, Both player's bet has been returned")
                    return
                await wait.edit(content = f"{player_1} has chosen an item")

                def check_r(reaction, user):
                    if reaction.message == dm and user.id == opponent_id :
                        return True

                if i == 1:
                    break

                player_1 = opponent
                opponent = player
                dm_check1 = dm_check2
                dm = await opp.send(embed=embed)
            weapon = dm_check1[0]
            for n in range(2):
                for i in range(4):
                    if str(weapon) == weapons_list1[i][1]:
                        if weapons_list1[i][2] == "DEF":
                            def_2 = weapons_list1[i][3]
                            type_2 = 'DEF'
                        elif weapons_list1[i][2] == "Rdc":
                            rdc_2 = weapons_list1[i][3]
                            if no_2 < weapons_list1[i][5]:
                                no_2 = weapons_list1[i][5] - 1
                            else:
                                no_2 = weapons_list1[i][5]
                            type_2 = 'Speed reduction'
                        else:
                            atk_2 = weapons_list1[i][3]
                            type_2 = 'ATK'

                        spd_2 = weapons_list1[i][5]
                        weapon_2 = weapons_list1[i][0]
                        ab_type2 = weapons_list1[i][4]

                        if n == 1:
                            break
                        try:
                            def_1 = def_2
                        except:
                            pass
                        try:
                            no_1 = no_2
                        except:
                            pass
                        try:
                            rdc_1 = rdc_2
                        except:
                            pass
                        try:
                            atk_1 = atk_2
                        except:
                            pass
                        weapon_1 = weapon_2
                        spd_1 = spd_2
                        type_1 = type_2
                        ab_type1 = ab_type2

                weapon = dm_check2[0]

            await asyncio.sleep(2)
            opponent1 = opponent
            opponent = player_1
            player = opponent1

            if spd_1 > spd_2:
                if type_1 == "ATK" and type_2 == "ATK":
                    health_2 = health_2 - atk_1
                    msg = f"{duel} {player}'s attack landed and reduced {opponent}'s health to **{health_2}**"
                elif weapon_1 == "Shield":
                    atk_1 = def_1
                    health_1 = health_1 + def_1 - atk_2
                    msg = f"{duel} {player} defended the attack and his health reduced to **{health_1}**"
                    if health_1 >= 100:
                        health_1 = 100
                        msg = f"{duel} {player} defended the attack completely"
                if weapon_2 == "Speed spell":
                    atk_2 = spd_2
                    spd_1 = spd_1 - rdc_2
                    no_2 = no_2 - 1
                    msg = f"{duel} {player}'s speed got reduced to **{spd_1}**"
                    health_1 = 100
                elif weapon_2 == "Shield":
                    atk_2 = def_2
                    health_2 = health_2 + def_2 - atk_1
                    msg = f"{duel} {opponent}'s defended the attack and his health reduced to **{health_2}**"

                await asyncio.sleep(2)
                await channel.send(f"""{duel} {player} chose **{weapon_1}**
        **{type_1} - {atk_1}**
        **{ab_type1} - {spd_1}**""")
                await asyncio.sleep(2)
                await channel.send(f"""{duel} {opponent} chose **{weapon_2}**
        **{type_2} - {atk_2}**
        **{ab_type2} - {spd_2}**""")
                await asyncio.sleep(2)
                await channel.send(msg)

                if health_1 < 0:
                    health_1 = 0
                elif health_2 < 0:
                    health_2 = 0

            elif spd_2 > spd_1:
                if type_1 == "ATK" and type_2 == "ATK":
                    health_1 = health_1 - atk_2
                    msg = f"{duel} {opponent}'s attack landed and reduced {player}'s health to **{health_1}**"
                elif weapon_2 == "Shield":
                    atk_2 = def_2
                    health_2 = health_2 + def_2 - atk_1
                    msg = f"{duel} {opponent} defended the attack and his health reduced to **{health_2}**"
                    if health_2 >= 100:
                        health_2 = 100
                        msg = f"{duel} {opponent} defended the attack completely"
                if weapon_1 == "Speed spell":
                    atk_1 = spd_1
                    no_1 = no_1 - 1
                    spd_2 = spd_2 - rdc_1
                    msg = f"{duel} {opponent}'s speed got reduced to **{spd_2}**"
                    health_2 = 100
                elif weapon_1 == "Shield":
                    atk_1 = def_1
                    health_1 = health_1 + def_1 - atk_2
                    msg = f"{duel} {player}'s defended the attack and his health reduced to **{health_1}**"

                await asyncio.sleep(2)
                await channel.send(f"""{duel} {opponent} chose **{weapon_2}**
        **{type_2} - {atk_2}**
        **{ab_type2} - {spd_2}**""")
                await asyncio.sleep(2)
                await channel.send(f"""{duel} {player} chose **{weapon_1}**
        **{type_1} - {atk_1}**
        **{ab_type1} - {spd_1}**""")
                await asyncio.sleep(1)
                await channel.send(msg)

                if health_1 < 0:
                    health_1 = 0
                elif health_2 < 0:
                    health_2 = 0

            elif spd_1 == spd_2:
                if type_1 == "DEF":
                    msg = f"Nothing happened, you both scared {waiting}"
                elif type_1 == "ATK":
                    print('yes')
                    health_1 = health_1 - atk_2
                    health_2 = health_2 - atk_1
                    msg = f"""{duel} Both player's attack landed
        {duel} Both player's health reduced to **{health_1}**"""
                elif type_1 == "Speed reduction":
                    spd_1 = spd_1 - rdc_2
                    spd_2 = spd_2 - rdc_1
                    msg = f"""{duel} Both player's speed reduced by **{spd_1}**"""

                await asyncio.sleep(2)
                await channel.send(f"""{duel} Both players chose **{weapon_1}** 
        **{type_1} - {atk_1}** 
        **{ab_type1} - {spd_1}**""")
                await asyncio.sleep(2)
                await ctx.send(msg)

                if health_1 < 0:
                    health_1 = 0
                elif health_2 < 0:
                    health_2 = 0

            profit = bet*2

            if num >= 1:
                if health_1 == 0:
                    add_coin(opponent_id, profit)
                    await ctx.send(f"{player} lost the duel")
                    await ctx.send(f"{opponent} won and got {profit}")
                elif health_2 == 0:
                    add_coin(player_id , profit)
                    await ctx.send(f"{opponent} lost the duel")
                    await ctx.send(f"{player} won and got {profit}")
                elif health_1 == 0 and health_2 == 0:
                    await ctx.send(f"Both players lost all their health, it's a draw")
            if num == 2:
                if health_1 > health_2:
                    add_coin(player_id , profit)
                    await ctx.send(f"{player} won the duel and got {profit} {reco}")
                    await ctx.send(f"{opponent} lost the duel and {bet} {reco}")
                elif health_2 > health_1:
                    add_coin(opponent_id, profit)
                    await ctx.send(f"{opponent} won the duel and got {profit} {reco}")
                    await ctx.send(f"{player} lost the duel and {bet} {reco}")
                else:
                    await ctx.send(f"It's a draw, bets returned")


async def setup(bot):
    await bot.add_cog(Economy(bot))
