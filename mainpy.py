from email import message
from pydoc import doc
from tabnanny import check
from urllib import response
import discord
import asyncio
import random
import os
import os.path
from os import path
from discord.ext import commands
import csv
import RockPaperScissorsDeerHacks

#Creates database if non exists
def CreateCSVDB():
    with open('db.csv','w+') as csvfile:
        header = ['user','amount']
        writer = csv.DictWriter(csvfile,fieldnames=header)
        writer.writeheader()
        return

def IsUserInDataBase(username):
    with open('db.csv', 'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if username in row['user']:
                return True
        return False

def CreateUserInDB(user):
    with open('db.csv','a',newline='') as csvfile:
        header = ['user','amount']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        row = {'user':user,'amount':500}
        writer.writerow(row)
        return

def CheckBalance(username):
    with open('db.csv', 'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if username in row['user']:
                print(row['amount'])
                return row['amount']


def PlayRPS(playerAction=str):
    RPSGame = RockPaperScissorsDeerHacks.RPS()
    RPSGame.Play(playerAction)
    print(f'{RPSGame.outcome}')
    return RPSGame.compChoice,RPSGame.outcome


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('we have logged in as {0.user}'.format(bot))
    if (path.exists('db.csv') == False):
        CreateCSVDB()
        print("Created new csv file")

@bot.command()
async def create(ctx):
    user = str(ctx.author).split('#')[0]
    userIn = IsUserInDataBase(user)
    if(userIn == False):
        CreateUserInDB(user)
        await ctx.channel.send("Successful made an account!")
        return
    elif(userIn == True):
        await ctx.channel.send("You already made an account.")
        return

@bot.command()
async def checkbalance(ctx):
    user = str(ctx.author).split('#')[0]
    await ctx.channel.send(f'Your balance is: {CheckBalance(user)}')

@bot.command()
async def hello(ctx):
    user = str(ctx.author).split('#')[0]
    await ctx.channel.send(f'Hello {user}!')

@bot.command()
async def goodbye(ctx):
    user = str(ctx.author).split('#')[0]
    await ctx.channel.send(f'See you later {user}!')

@bot.command()
async def randomnum(ctx):
    response = f"This is your random number: {random.randrange(1000)}"
    await ctx.channel.send(response)

@bot.command()
async def rps(ctx):
        user = str(ctx.author).split('#')[0]
        userIn = IsUserInDataBase(user)
        if(userIn==True):
                await ctx.channel.send('Please choose between "Rock","Paper","Scissors"')
                try:
                    userAction = await bot.wait_for('message',check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
                except asyncio.TimeoutError:
                    await ctx.channel.send("Ouch you ignored me :(")
                else:
                    if (userAction.content.lower() == "rock") or (userAction.content.lower() == "paper") or (userAction.content.lower() == "scissors"):
                        compChoice,outcome = PlayRPS(userAction)
                        await ctx.channel.send(f'You chose: {userAction.content.lower()}\nComputer picked: {compChoice.lower()}\nYou {outcome}!')
                    else:
                        await ctx.channel.send("Invaild choice try again")

            
bot.run(os.getenv('TOKEN'))