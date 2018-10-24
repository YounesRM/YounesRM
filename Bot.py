import discord
import asyncio
import requests
import http.client
import json
import urllib.request
from discord.ext import commands

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '47812a579a3b4d9a938da8fa57ad6458' }
connection.request('GET', '/v2/competitions/', None, headers )
response = json.loads(connection.getresponse().read().decode())


client = discord.Client()
bot = commands.Bot(command_prefix='$', description = 'helloworld')

@client.event
async def on_message(message):
  
    # we do not want the bot to reply to itself
    if message.author == client.user:
      return
      

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
        
    if message.content.startswith('!name'):
      global x
      x = 0
      
      for c in response['competitions']:
        
        msg = response['competitions'][x]['area']['name'].format(message)
        await client.send_message(message.channel, msg)
        x = x + 1  
    
    
    if message.content.startswith('!cinema'):
      msg = 'Give me your PostCode to find the Cinemas near You'.format(message)
      await client.send_message(message.channel, msg)
      
      postcode = await client.wait_for_message(timeout=20.0, author=message.author)
      if postcode is None:
            fmt = 'Sorry, you took too long. Call me Again'
            await client.send_message(message.channel, fmt.format(message))
            return
      else:
        address = 'https://api.cinelist.co.uk/search/cinemas/postcode/' + str(postcode.content)
        with urllib.request.urlopen(address) as url:
          
          cinema = json.loads(url.read().decode())
        
        global z
        z = 0
        for d in cinema['cinemas']:
          msg = cinema['cinemas'][z]['name'].format(message)
          await client.send_message(message.channel, msg)
          z = z + 1
    
    if message.content.startswith('!editme'):
        msg = await client.send_message(message.author, '10')
        await asyncio.sleep(3)
        await client.edit_message(msg, '40')

        
        
@client.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{1.content}'
    await client.send_message(after.channel, fmt.format(after, before))
   
  
  

@bot.command()
async def add(left : int , right : int):
  await bot.say(left + right)




  
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

client.run('NTAzOTgyNDA4MTQwMzI0ODY1.Dq-1Jw.lOYHE8LSpXpOjuaRD7qW8KAbZYM')
