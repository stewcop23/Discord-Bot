import discord
import pathlib
import random
import time
from datetime import datetime
import pytz
from threading import Thread

on = True
TOKEN = pathlib.Path('TOKEN.txt').read_text()
client = discord.Client()


def wait(sec, message):
    global on
    on = False
    time.sleep(sec*60)
    print('sleep over')
    if not on:
        client.loop.create_task(message.channel.send('Its Britney bitch'))
    on = True


def unit_conversion(input: str) -> str:

    parts = input.split(' ')
    try:
        num = int(parts[1])
        origional_num = num
        unit_from = parts[2]
        unit_to = parts[4]
    except:
        return 'ya fucked up mate, check your spelling'
    temp = ['c', 'f', 'k']
    dist = ['m', 'km', 'cm', 'in', 'ft', 'yd', 'mi']
    speed = ['m/s', 'km/h', 'mi/h']
    volume = ['l', 'oz', 'cup', 'gal', 'qt', 'pt', 'ml']

    if unit_to in temp:
        if unit_from == 'k':
            num = num - 273.15
        if unit_from == 'f':
            num = (num - 32)*(5/9)

        if unit_to == 'f':
            num = (num * (9/5))+32
        if unit_to == 'k':
            num += 273.15

    if unit_to in dist:
        if unit_from == 'km':
            num *= 1000
        elif unit_from == 'cm':
            num /= 100
        elif unit_from == 'in':
            num /= 39.37
        elif unit_from == 'ft':
            num /= 3.281
        elif unit_from == 'yd':
            num /= 1.094
        elif unit_from == 'mi':
            num *= 1609

        if unit_to == 'km':
            num /= 1000
        elif unit_to == 'cm':
            num *= 100
        elif unit_to == 'in':
            num *= 39.37
        elif unit_to == 'ft':
            num *= 3.281
        elif unit_to == 'yd':
            num *= 1.094
        elif unit_to == 'mi':
            num /= 1609

    if unit_to in speed:
        if unit_from == 'km/h':
            num /= 3.6
        elif unit_from == 'mi/h':
            num /= 2.237

        if unit_to == 'km/h':
            num *= 3.6
        elif unit_to == 'mi/h':
            num *= 2.237

    if unit_to in volume:
        if unit_from == 'oz':
            num /= 33.814
        elif unit_from == 'cup':
            num /= 4.167
        elif unit_from == 'gal':
            num *= 3.785
        elif unit_from == 'qt':
            num /= 1.057
        elif unit_from == 'pt':
            num /= 2.113
        elif unit_from == 'ml':
            num /= 1000

        if unit_to == 'oz':
            num *= 33.814
        elif unit_to == 'cup':
            num *= 4.167
        elif unit_to == 'gal':
            num /= 3.785
        elif unit_to == 'qt':
            num *= 1.057
        elif unit_to == 'pt':
            num *= 2.113
        elif unit_to == 'ml':
            num *= 1000

    return f' {origional_num} {unit_from} is {round(num*100)/100} {unit_to}'


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
        if channel == 'bot-controls':

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

                pacific = pytz.timezone('Canada/Pacific')
                pacTime = datetime.now(pacific).strftime("%H:%M:%S")

                aussie = pytz.timezone('Australia/NSW')
                ausTime = datetime.now(aussie).strftime("%H:%M:%S")

                ed = pytz.timezone('America/New_York')
                edt = datetime.now(ed).strftime("%H:%M:%S")

                eng = pytz.timezone("Etc/GMT")
                engtime = datetime.now(eng).strftime("%H:%M:%S")

                leb = pytz.timezone('Etc/GMT-3')
                lebtime = datetime.now(leb).strftime("%H:%M:%S")

                print(username, 'used time')
                print('^', pacTime, ausTime, edt, engtime, lebtime)
                await message.channel.send(f'24Hr (H:M:S) time in: \n Western Canada/USA: {pacTime} \n New Jeresy: {edt} \n England: {engtime} \n Lebanon: {lebtime} \n Sydney: {ausTime}')

# ----------- Basic Responces --------------
            basic_responces = {'gay': f'{username} is gay :rainbow_flag:',
                               'trans': f'{username} is trans :transgender_flag:',
                               'fish': f'{username} is forcing us to pretend that this is a planetary body',
                               'chock-a-block': 'The lights may be cactus'}

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


# ---------Swearing Responses------------
        swears = ['fuck', 'shit', 'cock', 'cunt',
                  'bitch', 'bullshit', 'dick', 'pussy', 'stfu']
        for word in swears:
            for _ in range(user_message.count(word)):
                chance = random.randint(1, 10)
                print(username, 'swore', chance)
                if chance <= 5:
                    if chance <= 1:
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
# ----------Slay-----------
        # if user_message == 'slay':
        for _ in range(user_message.count('slay')):
            roll = random.randint(1, 100)
            print(username, 'slayed', roll)
            if roll == 1:
                roll = random.randint(0, 2)
                print(f'^roll: {roll}')
                if roll > 0:
                    await message.channel.send('I will slay you')
                else:
                    await message.channel.send('SLAY YOUR EMEMIES! VANQUISH YOUR FOES!')
            elif roll <= 50:
                await message.channel.send(':sparkles:slay:sparkles:')


client.run(TOKEN)
