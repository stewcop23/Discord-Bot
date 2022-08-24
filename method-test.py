import discord
import time
from threading import Thread


def wait(sec):
    global on
    on = False
    time.sleep(sec*60)
    print('sleep over')
    on = True

TOKEN = 'MTAwNzQzNDI3MjEyODM4MTA2OA.GY8ze1.oEdJ52ALWqEc4J-JFdh4BGSgiY4ZQ803HFWDok'
on = True
client = discord.Client()
args=[0]
wait_thread = Thread(target=wait,args=args)

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
    if not on and channel == 'bot-controls' and user_message =='awake':
        on = True
        print('a')
        
    
    if channel == 'bot-controls'and on:
        if user_message.lower() == 'test':
            await message.channel.send('test')
        
        if user_message.lower().split(' ')[0]=='sleep':
            
            waitlength = float(user_message.lower().split(' ')[1])
            
            print(f'{username} made me sleep for {waitlength} minutes')
            args = [waitlength]
            wait_thread = Thread(target=wait,args=args)
            wait_thread.start()
            
            
    
client.run(TOKEN)