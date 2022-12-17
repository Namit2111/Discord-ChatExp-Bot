import discord
import score
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
       
    

    inc(message.author.id,message.content) 
    if message.content.startswith('.help'):
        await message.channel.send('.register to regiter yourslef for exp gain\n.view to see the score\n')
    if message.content.startswith('.register'):
      check = score.check(message.author.id)
      if check == True:
        await message.channel.send("Already registered")
      else:
        score.register(message.author.id)
        await message.channel.send("registered")
    if message.content.startswith('.score'):
      await message.channel.send(score.final_score(message.author.id))
    
def inc(id,msg):
  score.increase_score(id,msg)
      
    
client.run('MTA1MzAxMTg0MjcwNTkzNjUxNw.G8YWbx.tDMkG0yFQTKAsx99fuhnRZousPQq7pNt5dBd8Y')

