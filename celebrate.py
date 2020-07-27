#!/usr/bin/python3

# Imports basic python function libraries
import time

# Imports discord functions.  See https://pypi.org/project/discord.py/
import discord

# Imports file (celebratecredentials.py) that stores bot credentials (clientID, client secret, and token)
from celebratecredentials import *

# Clients are the connection to Discord websocket and API.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.
class bot(discord.Client):

    bolNotCelebrated = True

# Provides time stamp and bot information upon successful log-in.    
# https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready

    async def on_ready(self):
        print(time.asctime())
        print('Logged in as')
        print(Client.user.name)
        print(Client.user.id)
        print('------')

# Bot behavoir when a message is seen.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Message
# https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message
    async def on_message(self, message):

        # Ignores messages sent by the bot.
        if message.author.id == self.user.id:
            return

        # Respnd when bot is mentioned and send PM to BOT manager to register a new celebration entry.
        if Client.user.mentioned_in(message):
            
            # Acknowledge the message
            await message.channel.send('Hi {}!'.format(message.author))
            
            # Inform BOT manager of mention
            userPhoenix = Client.get_user(203445784899878912)
            await userPhoenix.send('Phoenix, {} (UserID {}) said: **"{}"** on server "{}" (serverID {}) - Channel "{}" (channelID {})'.format(message.author, message.author.id, message.content, message.guild, message.guild.id, message.channel, message.channel.id,))
            
        # If the celebrate messages have not been sent, call the celebrate function.  If they have, setup for the next month.

        if time.strftime('%d') != 1: # Checks to see if it's the first of the month or not.  If so, run funcCelebrate() if it hasn't already been run before.
            bolNotCelebrated = True
            
        elif bolNotCelebrated == False:
            await funcCelebrate()
            
async def funcCelebrate():

    print('funcCelebrate')

    # Initilizes variables
    varUser = Client.get_user(203445784899878912) # Defaults to Phoenix's user
    varChannel = Client.get_channel(698557706574888972) # Defaults to Phoenix's Testing Channel
    varMonth = time.strftime('%B') # Sets varMonth to current month in verbose form.

    # Sends heartbeat message to Phoenix
    await varUser.send('Congratulations, it is now {}'.format(varMonth))

    # Each month has it's own tree, and within each tree is every event to be celebrated.  To add more events, copy/paste the following, inserting the appropriate userID (xxxx), channelID (yyyy), and message (zzzz)
    # varUser = Client.get_user(xxxx)
    # varChannel = Client.get_channel(yyyy)
    # await varChannel.send('zzzz')
    # varUser = Client.get_user(203445784899878912) # Defaults to Phoenix's user
    # varChannel = Client.get_channel(698557706574888972) # Defaults to Phoenix's Testing Channel
    
    if varMonth == "January":
        print('Congratulations, it is now {}1'.format(varMonth))
    elif varMonth == "February":
        print('Congratulations, it is now {}2'.format(varMonth))
    elif varMonth == "March":
        print('Congratulations, it is now {}3'.format(varMonth))
    elif varMonth == "April":
        print('Congratulations, it is now {}4'.format(varMonth))
    elif varMonth == "May":
        print('Congratulations, it is now {}5'.format(varMonth))
    elif varMonth == "June":
        print('Congratulations, it is now {}6'.format(varMonth))
    elif varMonth == "July":
        print('Congratulations, it is now {}7'.format(varMonth))
    elif varMonth == "August":
        print('Congratulations, it is now {}8'.format(varMonth))
    elif varMonth == "September":
        print('Congratulations, it is now {}9'.format(varMonth))
    elif varMonth == "October":
        print('Congratulations, it is now {}10'.format(varMonth))
    elif varMonth == "November":
        print('Congratulations, it is now {}11'.format(varMonth))
    elif varMonth == "December":
        print('Congratulations, it is now {}12'.format(varMonth))
    else:
        print('Invalid Month')

# Instantiates classes
Client = bot()

# Starts bot with token from credentials file.  This must be the last command in the file.
Client.run(Token)
