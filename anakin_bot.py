# bot.py
import os
import pdb
from discord.utils import get
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='$')

@client.command()
async def tragedy(ctx):
        Tragedy = 'Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.'
        await ctx.author.send(Tragedy)

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

    if ' sand ' in message.content.lower():     #don't like sand
        await message.reply('I Don\'t Like Sand. It\'s Coarse And Rough And Irritating And It Gets Everywhere.')
    
    if 'you\'ve grown' in message.content.lower():      #grown beautiful
        await message.reply('So have you, grown more beautiful… for a senator, I mean.')

    if ' is evil' in message.content.lower():       #point of view
        await message.reply('From my point of view, the Jedi are evil.')

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

    await client.process_commands(message) 

client.run(TOKEN) 
