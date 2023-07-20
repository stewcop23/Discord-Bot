import discord
import pathlib
import random
import time
from datetime import datetime
import pytz
from threading import Thread
import re


on = True
TOKEN = pathlib.Path('TOKEN.txt').read_text()
client = discord.Client()

# ratio between unit to base unit(this number will be multiplied with the origional number to give the base unit)
units = {'m': 1, 'km': 1000, 'cm': (1/100), 'in': (1/39.37), 'ft': (1/3.281), 'yd': (1/1.094), 'mi': 1609,
         'm/s': 1, 'km/h': (1/3.6), 'mi/h': (1/2.237),
         'l': 1, 'ml': (1/1000), 'oz': (1/33.814), 'cup': (1/4.167), 'cups': (1/4.167), 'gal': (3.785), 'qt': (1/1.057), 'pt': (1/2.113),
         'g': 1, 'kg': 1000, 'mg': (1/1000), 'lb': 453.6}

times = {"Western Canada/USA": 'Canada/Pacific', "New Jersey": 'America/New_York',
         "England": "Etc/GMT", "Lebanon": 'Etc/GMT-3', "Sydney": 'Australia/NSW'}

swearing_chance = 0.5
slay_chance = 0.5
def wait(sec, message):
    global on
    on = False
    time.sleep(sec*60)
    print('sleep over')
    if not on:
        client.loop.create_task(message.channel.send('Its Britney bitch'))
    on = True


def unit_conversion(input: str) -> str:
    done = False
    parts = input.split(' ')
    try:
        num = int(parts[1])
        origional_num = num
        unit_from = parts[2]
        unit_to = parts[4]
    except Exception:
        return 'ya fucked up mate, check your spelling'

    temp = ['c', 'f', 'k']
# temp has to be done differently cuz the zeroes arent the same
    if unit_to in temp:
        if unit_from == 'f':
            num = (num - 32)*(5/9)
        elif unit_from == 'k':
            num -= 273.15

        if unit_to == 'f':
            num = (num * (9/5))+32
        elif unit_to == 'k':
            num += 273.15
        done = True

    elif unit_from in units:
        num *= units[unit_from]
        if unit_to in units:
            num /= units[unit_to]
            done = True

    if done:
        return f' {origional_num} {unit_from} is {round(num*100)/100} {unit_to}'
    else:
        return 'I dont know one of those units'


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global on
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content).lower()

    if message.author == client.user:
        return

    if not on and channel == 'bot-controls' and user_message == 'awake':

        on = True
        await message.channel.send('Its Britney bitch')
        print('a')

    if on:
        global swearing_chance
        global slay_chance
        # ---------Swearing Responses------------
        swears = ['fuck', 'shit', 'cock', 'cunt',
                  'bitch', 'bullshit', 'dick', 'pussy', 'stfu']
        for word in swears:
            for _ in range(user_message.count(word)):
                chance = random.random()
                print(username, 'swore', round(chance,2))
                if chance <= swearing_chance:
                    if chance <= (swearing_chance/100):
                        await message.channel.send(f'{message.author.mention}, NO FUCKING SWEARING')
                        print('^sweary warning sent')
                    else:
                        await message.channel.send(f'{message.author.mention}, NO SWEARING')
                        print('^ warning sent')

# ---------Thankful/Apllologetic Responses------------
        nice_words = {'thanks': 'you\'re welcome', 'cheers': 'no problem',
                      'sorry': 'it\'s ok', 'im sad': 'it\'s ok', 'hi': 'hi'}

        for word in nice_words:
            if f'{str(word)} jim' in user_message:
                print(username, 'said', word)
                await message.channel.send(f'{nice_words[word]} {username}')
                
                
#----------------Activate Jim-----------------------
        if user_message == 'activate jim':
            await message.channel.send('activated')
            loopable = True
            while loopable == True:
                tosend = input("Send: ")
                if tosend == "its over":
                    loopable = False
                    print("Jim is now turned off")
                elif len(tosend) > 0:
                    await message.channel.send(f'{tosend}')
                    print(f"sent \"{tosend}\"")
# ----------Slay-----------
        for _ in range(user_message.count('slay')):
            roll = random.random()
            print(username, 'slayed', round(roll,2))
            if roll > .95:
                roll = random.randint(0, 2)
                print(f'^roll: {roll}')
                if roll > 0:
                    await message.channel.send('I will slay you')
                else:
                    await message.channel.send('SLAY YOUR EMEMIES! VANQUISH YOUR FOES!')
            elif roll <= slay_chance:
                await message.channel.send(':sparkles:slay:sparkles:')
        
        if channel == 'bot-controls':

#------- Swearing updating -------
            if re.search("^update swearing",user_message.lower()) is not None:
                swearing_chance = float(user_message.split(' ')[2])
                print(f'{username} has updated swearing chance to {swearing_chance}')
                await message.channel.send(f'swearing response chance is now {swearing_chance}')

#------- Query swearing  ---------
            if re.search("^check swearing",user_message.lower()) is not None:
                print(f'{username} has asked to check the swearing chance ({swearing_chance})')
                await message.channel.send(f'swearing response is {swearing_chance}')

#--------- Slay Updating -------
            if re.search("^update slay",user_message.lower()) is not None:
                slay_chance = float(user_message.split(' ')[2])
                print(f'{username} has updated slay chance to {slay_chance}')
                await message.channel.send(f'slay response chance is now {slay_chance}')

#----------- Query Slay ----------
            if re.search("^check slay",user_message.lower()) is not None:
                print(f'{username} has asked to check the slay chance ({slay_chance})')
                await message.channel.send(f'slay response is {slay_chance}')

#--------- Alive-ness test -----
            if user_message == 'test':
                await message.channel.send('test')

# ----------- Sleep -----------
            if user_message.split(' ')[0] == 'sleep':

                waitlength = float(user_message.split(' ')[1])
                await message.channel.send(f'sleeping for {waitlength}')
                print(f'{username} made me sleep for {waitlength} minutes')
                args = [waitlength, message]
                wait_thread = Thread(target=wait, args=args)
                wait_thread.start()

# ----------- Time -----------
            if user_message == 'time':

                timeline = ""
                for zone in times:
                    timeline += zone + ": " + datetime.now(pytz.timezone(times[zone])).strftime("%H:%M:%S") + "\n"

                print(username, 'used time')
                await message.channel.send(f'24Hr (H:M:S) time in: \n{timeline}')

# ----------- Basic Responces --------------
            basic_responces = {'gay': f'{username} is gay :rainbow_flag:',
                               'trans': f'{username} is trans :transgender_flag:',
                               'fish': f'{username} is forcing us to pretend that this is a planetary body',
                               'chock-a-block': 'The lights may be cactus',
                               "is jim there?":"Hello yes I am alive"}

            for word in basic_responces:
                if user_message == word:
                    await message.channel.send(basic_responces[word])
                    print(username, 'used', word)

# ----------- Unit Conversion -------
            if 'convert' == user_message.split(' ')[0]:
                response = unit_conversion(user_message.lower())
                # convert 15 C to F

                print(f'{username}: {response}')
                await message.channel.send(response)

# ----------- Squirrel -----------
            if user_message == 'squirrel':
                print(username, 'used squrrel')
                eat = random.randint(1, 10)
                print('^', eat)
                if eat > 4:
                    print('^', 'cute')
                    await message.channel.send('so cute!')

                elif eat > 1:
                    print('^', 'smol')
                    await message.channel.send('so smol')

                else:
                    print('^', 'edible')
                    await message.channel.send('you should eat that')





client.run(TOKEN)
