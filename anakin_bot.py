# bot.py
import os
import pdb
from discord.utils import get
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')   #Prints connected to discord
    for guild in client.guilds:
        if guild.name == GUILD:
                break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'                 #prints connected to Campsite
    )

@client.event
async def on_message(message):
    if message.author == client.user:
                return
            
    if 'hello there' in message.content.lower():    #general Kenobi response
        await message.reply('General Kenobi!', mention_author=True)

    if message.content.startswith('Do it') or message.content.startswith('do it'):  #dewit emoji reaction
        dewit = '<:dewit:431109222441287690>'
        await message.add_reaction(dewit)

    if 'men' in message.content.lower():    #Men + women + children
        og_msg = message.content
        words = og_msg.split(' ')                       #splits message into individualt words based on spaces
        for men_location, string in enumerate(words):   #needed to find 'men' substring on a word in the message
            if 'men' in string:
                men_found = men_location
        men_word = words[men_found]                     #returns original word with 'men' substring
        men_split = men_word.split('men')               #splits original word to before and after 'men' substring
        women_msg = 'Not just the ' + men_word + ' but the ' + men_split[0] + 'women' + men_split[1] + ' and the ' + men_split[0] + 'children' + men_split[1] + ' too!' #build output message string
        await message.reply(women_msg,mention_author=True)

client.run(TOKEN) 
