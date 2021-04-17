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

@client.command(help='Send user a story not told by Jedi.')     #send user a story not told by Jedi 
async def tragedy(ctx):
        Tragedy = 'Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.'
        await ctx.author.send(Tragedy)

@client.command(help='Send user video link based on argument provided.')       #send user video link
async def video(ctx, arg):
    send_link = False
    arg_opt = ['help: List options', '1: Rogue One Ending', '2: Seagulls', '3: Coming soon']
    if arg.lower() == '1':
        embed=discord.Embed(title='Rogue One slightly alternative ending', url='https://youtu.be/XWBpWN5SKRY', description='', color=0xFF5733)
        send_link = True

    elif  arg.lower() == '2':
        embed=discord.Embed(title='SEAGULLS! (Stop It Now)', url='https://youtu.be/U9t-slLl30E', description='', color=0xFF5733)
        send_link = True

#    elif arg.lower() == 'help':     #help option probably improperly implemented
#        await ctx.author.send('The following are valid options:')
#        send_link = False

    elif  arg.lower() == 'help':
        await ctx.author.send(arg_opt)
        send_link = False

    else:
        await ctx.message.reply('Not a valid argument for video command! \nTry $video help')
        send_link = False

    if send_link == True:
        await ctx.message.reply('If into the security recordings you go. Only pain will you find')
        await ctx.author.send(embed=embed)  #sends link
        send_link == False

@client.event       #command error handling
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):     #command not found
        await ctx.send('Not a valid command')
    if isinstance(error, commands.MissingRequiredArgument):        #missing argument
        await ctx.send('Please provide an argument for command in quotes ex. $video \"help\"')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')   #Prints connected to discord
    for guild in client.guilds:
        if guild.name == GUILD:
                break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'                 #prints connected to server
    )
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='through the lies of the Jedi'))

@client.event
async def on_message(message):
    if message.author == client.user:
                return

    if 'hello there' in message.content.lower():    #general Kenobi response
        await message.reply('General Kenobi!', mention_author=True)

    if message.content.startswith('Do it') or message.content.startswith('do it'):  #dewit emoji reaction
        dewit = '<:dewit:431109222441287690>'
        await message.add_reaction(dewit)

    if ' sand' in message.content.lower() or ' sandy' in message.content.lower():     #don't like sand
        await message.reply('I Don\'t Like Sand. It\'s Coarse And Rough And Irritating And It Gets Everywhere.')
    
    if 'you\'ve grown' in message.content.lower() or 'you have grown' in message.content.lower():      #grown beautiful
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

    if 'what are we going to do' in message.content.lower():        #returns youngling GIF
        embed=discord.Embed(description='', color=discord.Color.blue())
        embed.set_image(url='https://i.imgur.com/plUr2WC.gif')
        await message.reply(embed=embed)

    if message.attachments:     #reply if attachment present
        await message.reply('Attachment is forbidden. Possession is forbidden. Compassion, which I would define as unconditional love, is essential to a Jedi’s life. So you might say, that we are encouraged to love.')

    await client.process_commands(message) 

client.run(TOKEN) 
