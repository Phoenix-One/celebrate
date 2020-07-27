#!/usr/bin/python3

# Imports basic python function libraries
import time

# Imports discord functions.  See https://pypi.org/project/discord.py/
import discord

# Imports file (celebratecredentials.py) that stores bot credentials (clientID, client secret, and token)
from celebratecredentials import *

# Imports manuallog.py, where the speciic events are stored.
from manuallog import *

# Clients are the connection to Discord websocket and API.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.
class bot(discord.Client):

    bolNotCelebrated = True

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

        # If the celebrate messages have not been sent, call the celebrate function.  If they have, setup for the next month.
        if (time.strftime('%d') == 1):
            if bolNotCelebrated:
                celebrate()
        else:
            bolNotCelebrated = True
            celebrate()  #debugging call

        # Respnd to celebrate messages and send PM to BOT manager to register a new celebration log.
        if message.content.startswith('Maia, celebrate'):
            userAuthor = message.author.mention
            await message.channel.send('Will do, {}'.format(userAuthor))
            userPhoenix = client.get_user(203445784899878912)
            await userPhoenix.send('Phoenix, {} said: " {}" on serverID {} - channelID {}.  Their userID is: {}'.format(message.author, message.content, message.guild.id, message.channel.id, message.author.id))

# Instantiates classes
client = bot()

# Starts bot with token from credentials file.  This must be the last command in the file.
client.run(Token)
