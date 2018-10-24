# Younes RM Discord's Bot Project

This project will be using Python 3 programming lanuage and Discord servers to create a ChatBot which is able to communicate with the users and also learn at the same time as it gets new requests.

This is a Group project for Coventry University however i will provide the codes written by me seprately and also the whole complete project as well. all supposrt and contact will be available by my [GitHub Profile Page](https://github.com/younesrm)


```markdown
Used Libraries in Python Project

import discord
import asyncio
import requests
import http.client
import json
from discord.ext import commands
```

In this project we will be using APIs and Json files to recieve and work with datas all over the world based the request we revieve from our users. the example below is us sending a request in python to recieve the nearest cinemas based on the postcode given

```markdown 
APIs request and Json files
 
 address = 'https://api.cinelist.co.uk/search/cinemas/postcode/' + str(postcode.content)
 with urllib.request.urlopen(address) as url:
 cinema = json.loads(url.read().decode())
 
```

because we are working with Discord bots and the Discord Python library. it is a bit different on how we recieve data from the users. for an example we have wrote a code to activate the Find Cinema request and then recieve the users postcode and give our the cinemas near them base on it.


```markdown
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
  
```
so in the example above the bot gets activated when the users send "!cinema" command in the chat. after the bot will ask the user for their post code and will give them 20s to response. if the user does not gives a valid reason within 20s the bot will gets deactivated and will ask them to call the bot again for the command. but if the bot recieves the valid postcode then it will run the request file to revieve the data and saves the in a json file. from there for every cinema in the json file the bot will access the name and then send it as message one by one to the chat.
this project is in early stage the commands will have better quality and more security. for example we will add updates to check if the postcode is valid before we try the request and in case of an error rather than crashing we will send the user a message to tell them what was wrong. aslo in terms of the robot working in a large community we need to make sure one user calls the bot for a command we only recieve additional information from the same user not others. an example could be one user calling the Cinema command and another use sending a fake or different postcode within 20s then bot will work with the first message which is not from the person who called the command.
As i mentioned this project is currently in early progress therefore visit this page again for regular updates.

[Access to the full Python Code](https://github.com/YounesRM/YounesRM.github.io/blob/master/Bot.py)

## Younes RM

