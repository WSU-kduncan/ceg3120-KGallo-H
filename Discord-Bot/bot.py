import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Chinese_fortune_cookie = [
        'A beautiful, smart, and loving person will be coming into your life.',
        'A gambler not only will lose what he has, but also will lose what he doesn’t have.',
        'A golden egg of opportunity falls into your lap this month.',
        'A soft voice may be awfully persuasive.',
        'Advice, when most needed, is least heeded',
        'All will go well with your new project.',
        'Because you demand more from yourself, others respect you deeply.',
        'Do not be intimidated by the eloquence of others.',
        'Do not let ambitions overshadow small success.',
        'Don’t let the past and useless detail choke your existence.',
        'Every flower blooms in its own sweet time.',
        'First think of what you want to do; then do what you have to do.',
        'Fortune Not Found: Abort, Retry, Ignore?',
        'He who knows he has enough is rich.',
        'Fear and desire – two sides of the same coin.',
        'Expect much of yourself and little of others.',
        'It is better to be an optimist and proven a fool than to be a pessimist and be proven right.',

    ]

    star_wars_quotes = [
        'It’s the ship that made the Kessel run in less than twelve parsecs. I’ve outrun Imperial starships. Not the local bulk cruisers, mind you. I’m talking about the big Corellian ships, now. She’s fast enough for you, old man.'
        'I find your lack of faith disturbing.',
        'Do. Or do not. There is no try.',
        'There’s always a bigger fish.',
        'Fear is the path to the dark side. Fear leads to anger; anger leads to hate; hate leads to suffering. I sense much fear in you.',
        'I’m just a simple man trying to make my way in the universe.',
        
    ]
    I_hate_sand = [
         "I don't like sand. It's coarse, and rough, and irritating, and it gets everywhere.",
    ]
    if message.content == 'fortune!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(Chinese_fortune_cookie)
        await message.channel.send(response)

    if message.content == 'star wars!':
        response = random.choice(star_wars_quotes)
        await message.channel.send(response)

    if message.content == 'sand!':
            response = random.choice(I_hate_sand)
            await message.channel.send(response)

client.run(TOKEN)
