#!/usr/bin/python3

# Imports discord functions.  See https://pypi.org/project/discord.py/
import discord

# Imports file (celebratecredentials.py) that stores bot credentials (clientID, client secret, and token)
from celebratecredentials import *

# Clients are the connection to Discord websocket and API.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.
class bot(discord.Client):

# Provides bot name and ID upon successful log-in.    
# https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready

    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

# Bot behavoir when a message is seen.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Message
# https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message
    async def on_message(self, message):

        # Ignores messages sent by the bot.
        
        if message.author.id == self.user.id:
            return

        # Returns "World" when receiving "Hello" message
        if message.content.startswith('Hello'):
            await message.channel.send('World')

# Instantiates client
client = bot()

# Starts bot with token from credentials file.  This must be the last command in the file.
client.run(Token)
