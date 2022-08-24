import discord
import random
import time
from datetime import datetime
import pytz
from threading import Thread

on = True

TOKEN = 'MTAwNzQzNDI3MjEyODM4MTA2OA.GY8ze1.oEdJ52ALWqEc4J-JFdh4BGSgiY4ZQ803HFWDok'

client = discord.Client()


def wait(sec, message):
    global on
    on = False
    time.sleep(sec*60)
    print('sleep over')
    if not on:
        client.loop.create_task(message.channel.send('Its Britney bitch'))
    on = True


@client.event
async def on_ready():
    print('logged in as{0.user}'.format(client))


@client.event
async def on_message(message):
    global on
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if message.author == client.user:
        return
    
    if not on and channel == 'bot-controls' and user_message == 'awake':

        on = True
        await message.channel.send('Its Britney bitch')
        print('a')

    if on:
        if channel == 'bot-controls':

            if user_message.lower() == 'test':
                await message.channel.send('test')
                
#----------- Sleep -----------
            if user_message.lower().split(' ')[0] == 'sleep':

                waitlength = float(user_message.lower().split(' ')[1])
                await message.channel.send(f'sleeping for {waitlength}')
                print(f'{username} made me sleep for {waitlength} minutes')
                args = [waitlength, message]
                wait_thread = Thread(target=wait, args=args)
                wait_thread.start()
                
#----------- Time -----------
            if user_message.lower() == 'time':

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

#----------- Basic Responces --------------
            basic_responces = {'gay': f'{username} is gay :rainbow_flag:',
                               'trans': f'{username} is trans :transgender_flag:',
                               'fish': f'{username} is forcing us to pretend that this is a planetary body',
                               'chock-a-block': 'The lights may be cactus'}

            for word in basic_responces:
                if user_message.lower() == word:
                    await message.channel.send(basic_responces[word])
                    print(username, 'used', word)

#----------- Squirrel -----------
            if user_message.lower() == 'squirrel':
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

            
#---------Swearing Responses------------
        swears = ['fuck', 'shit', 'cock', 'cunt',
                  'bitch', 'bullshit', 'dick', 'pussy', 'stfu']
        for word in swears:
            for _ in range(user_message.lower().count(word)):
                chance = random.randint(1, 10)
                print(username, 'swore', chance)
                if chance <= 5:
                    if chance <= 1:
                        await message.channel.send(f'{message.author.mention}, NO FUCKING SWEARING')
                        print('^sweary warning sent')
                    else:
                        await message.channel.send(f'{message.author.mention}, NO SWEARING')
                        print('^ warning sent')
                        
#---------Thankful/Apllologetic Responses------------
        nice_words = {'thanks': 'you\'re welcome', 'cheers': 'no problem',
                      'sorry': 'it\'s ok', 'im sad': 'it\'s ok'}
        for word in nice_words:
            if f'{str(word)} jim' in user_message.lower():
                print(username, 'said', word)
                await message.channel.send(f'{nice_words[word]} {username}')


client.run(TOKEN)
