import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'oi' :
        await message.channel.send(f'Olá, {message.author.mention}!')

client.run('MTU1MzYwMTE5MjU4Njc3NjYwNg.GpJbU_.hAJXArKL6ydoQrnczfgmYv_-BjsvKh5FvNTsC0')

