import discord
import random

client = discord.Client()

key_words = ["Corey", """@Langie_Bot"""]

response_message = [
  "Corey is not available at the moment",
  "We are too busy to read your message",
  "Just give me one second",
  ]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # bot wont send messages if message is from said bot
  if message.author == client.user:
    return
  # bot says hey when hey message recongnized
  if message.content.startswith('hey'):
    await message.channel.send("""Heyyyyyyyyyyyyyy with a bunch of Y's!""")

  if message.content.startswith('hi'):
    await message.channel.send("""Hiiiiiiiiiiiiiiii with a bunch of I's!""")  

  
# when bot seeing key word, random response_message sent
  if any(word in message.content for word in key_words):
    await message.channel.send(random.choice(response_message))

# must store channel ID here.
client.run('OTQyODQzMDQzNzk3Njc2MDYz.YgqZAg.O4AHx34B168O339u3LLncvDrfiM') 
