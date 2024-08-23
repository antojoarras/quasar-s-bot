# ctx.send(f'Cleared {amount} messages.', delete_after=5)

import discord
from discord import Intents
import asyncio
import os
from discord.ext import commands
from config import Config as c

TOKEN = os.environ.get('TOKEN')

intents = Intents.all()

prefix = c.prefix
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready to work for you!')

@client.event
async def on_message(message):
    if (isinstance(message.channel, discord.DMChannel)):
        if (message.author.id == 1078713043069976666):
            await message.channel.send('I work...?')

    await client.process_commands(message)

if __name__ == "__main__":
    client.run(TOKEN)
