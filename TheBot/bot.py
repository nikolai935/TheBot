import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
token = open("key.txt", "r").read()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("{0.user} is online!".format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("awesome!"))

client.run(token)