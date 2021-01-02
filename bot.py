import discord
import random
from discord.ext import commands

token = open("token.txt", "r").read()  
client = commands.Bot(command_prefix = '+')

players = {}

insulte= [] #tableau à remplir d'insulte
citation = [] #tableau à remplir de savantes citations 
imagesanis = [] #tableau à remplir d'images
meme = [] #tableau à remplir de memes marrants

@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')  

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_clients_in(server)
    await voice_client.disconnect()

@client.event
async def on_message(message):  # event that happens per any message.
    
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "+respect" in message.content.lower():
        await message.channel.send('trql juste parle bien akhi')
        
    if "+insulte" in message.content.lower() or "+attaque" in message.content.lower() :
        await message.channel.send(random.choice(insulte))

        
    if "+citation" in message.content.lower():
        await message.channel.send(random.choice(citation))
        
    if "+freezer" in message.content.lower():
        with open("Freezer3rdform.png", 'rb') as fp:
            await message.channel.send("personne :\nabsolument personne :\nfreezer :")
            await message.channel.send(file=discord.File(fp, 'tareum.png'))
    
    if "anis" in message.content.lower() :
        emoji = '\U0001F4AF'
        await message.add_reaction(emoji)
        
    if "+image" in message.content.lower():
        with open(random.choice(imagesanis), 'rb') as fp:
            await message.channel.send(file=discord.File(fp, 'ANISANIS.png'))
            
    if "+meme" in message.content.lower():
        with open(random.choice(meme), 'rb') as fp:
            await message.channel.send(file=discord.File(fp, 'anismeme.png'))
    
    if "+whoru" in message.content.lower():
        await message.channel.send("Salam je suis le plus beau bot du monde\n\t\t`rafrafcorp 2020 tous droits reservés`")

client.run(token)  # recall my token was saved!