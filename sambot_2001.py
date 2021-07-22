# Using python 3.9
#import discord
from discord.ext import commands
import readLine
import fourletterphat as flp

token = readLine.read_line("token.txt", 0)
client = commands.Bot(command_prefix='.')
inVoicechat = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(f"{message.guild}: {message.channel}: {message.author}: {message.content}")
    # If the bot is the writer, don't do anything
    if message.author == client.user:
        return

    # on message makes it so that commands can't work unless I have this code
    await client.process_commands(message)


# if members new voicechat state == none, remove from list. Else add to list
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel == None:
        inVoicechat.remove(str(member))
    else:
        inVoicechat.append(str(member))

    flp.clear()
    flp.print_float(len(inVoicechat))
    


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def voiceChatCheck(ctx):
    voiceState = ctx.author.voice

    if voiceState:
        await ctx.send('YES')
    else:
        await ctx.send('no...')


client.run(token)
