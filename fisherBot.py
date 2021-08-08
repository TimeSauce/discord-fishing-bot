import discord
import random
import requests
import json
from bs4 import BeautifulSoup

TOKEN = "Discord Bot Code"
TENOR = "Tenor Api code"

fishingWords = ['fish', 'fishing', 'fishes']
fishHelp = ['fishhelp', 'fishinghelp', 'help with fish', 'fishes help']
fishFacts = ['fishfact', 'fishingfact', 'fishingfacts', 'fishfacts']

client = discord.Client()

# Logged in message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Discord reaction to messages
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    usermessage = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return
    
    if any(x in usermessage.lower() for x in fishHelp):
        await message.channel.send("Ahoy there laddies, I'm your friendly neighbour fisherman! \n I'll slide into the chat as soon as you start talking about mah fishes or you can ask me about fishing by writing: fishfact! \n Ah haha, Happy Fishing!")

    if any(x in usermessage.lower() for x in fishFacts):
        facts = []
        r = requests.get("http://anglingcouncilireland.ie/fun-facts-fishing/")
        soup = BeautifulSoup(r.content, "html.parser")
        soup1 = soup.find("div", class_= "entry-content")
        for li in soup1.find_all("li"):
            facts.append(li.text)
        rngfact = random.choice(facts)

        await message.channel.send("Did you know, that: " + rngfact)

    if any(x in usermessage.lower() for x in fishingWords):
        topicList = ['fishing', 'fish']
        randomChoice = random.choice(topicList)
        randomNumb = random.randrange(0, 50)
        r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (randomChoice, TENOR, str(50)))
        top = json.loads(r.content)
        await message.channel.send(top['results'][randomNumb]['media'][0]['gif']['url'])
        return

    if usermessage.lower() == 'ahoy':
        await message.channel.send(f'Ahoy there {username}')
        return

# Bot message when he joins
@client.event
async def on_guild_join(guild):
    joinchannel = guild.system_channel
    await joinchannel.send('*Ahoy everyone! I\'m very pleased, that you decided to invite me, for more help write: fishHelp !* \n\n I\'m a Bot, created by TimeSauce')


# Connecetion to bot
client.run(TOKEN)
