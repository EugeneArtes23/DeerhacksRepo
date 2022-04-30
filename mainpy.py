from urllib import response
import discord
import random
import requests

TOKEN = 'OTY5NzkyMjQ5MDMyNDc4Nzkw.Ymyjag.v9l6spz5gdtLiRPp-W8_oVE56w4'

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}.format{client}')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '!hello':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == '!bye':
        await message.channel.send(f'See you later {username}!')
    elif user_message.lower() == '!random':
        response = f"This is your random number: {random.randrange(1000)}"
        await message.channel.send(response)
        

client.run(TOKEN)