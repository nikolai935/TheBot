import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import requests

token = open("key.txt", "r").read()
BOT_PREFIX = ("!", "?", ".", ",")
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description='Answers a yes or no question',
                brief='Answers from beyond',
                aliases=['eightBall', 'eight-ball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    possibleResponse = [
        'That is a resounding no',
        'It is not loking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definetly'
    ]
    await ctx.send(random.choice(possibleResponse) + ", " + ctx.message.author.mention)

@client.command(name="sqr",
                description='Squares a givenn number',
                brief='square a number',
                aliases=['square'])
async def square(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value) + ", " +  ctx.message.author.mention)

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("awesome!"))

@client.command(name="bitcoin",
                description='Shows the bitcoin exchange rate in USD',
                brief='Shows bitcoin price',
                aliases=['bcoin', 'bc'])
async def bitcoin(ctx):
    url = 'http://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send("Bitcoin exchangerate is $" + value + ", " + ctx.message.author.mention)

@client.command(description='Shows latency between the server and the user',
                brief='Shows ping')
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(description='Rolls a dice', brief='Rolls a dice')
async def roll(ctx):
    await ctx.send(random.randint(1, 6))



client.run(token)