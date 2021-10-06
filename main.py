import discord, os, asyncio, datetime, requests, json, random

from discord.ext import tasks, commands

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + " -" + json_data[0] ['a']
  return(quote)


hello_type = ["sup", "Sup"]
sad_words = ["sad", "depressed", "unhappy", "angry", "deppressing"]
starter_encourangemens = ["cheer up!", "Hang in there", "you are a great person!"]

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))
  await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.Watching, name="Hemand Gaming"))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return



  msg = message.content

  if message.content.startswith('.hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('.inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encourangemens))
    
  if any(word in msg for word in hello_type):
    await message.channel.send('Hey Sup Its me HemandGamer bot :D')

  if message.content.startswith('.stop'):
    quit()

  client.run
  ('ODk1MTUyODc2NTY4MDgwMzk0.YV0aFA.t2DmIPpT1a7rx22UHBq6HAFBSuo')