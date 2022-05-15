import os
import discord
import json
from discord.ext import commands


f1 = open("details2.json")
userdata=json.load(f1)

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
  print('Bot is ready')



@bot.command(name = "find",
             help="Enter what you wish to know to get the names of right mentors. \nTry \n$find android flutter",
	brief="Returns the required mentor's names.\nTry \n$help find")
async def on_message(message,*,arg):
 # str(arg).lower()
  new = str(arg).lower().split()
  new.sort()
  output = ""
  if new:
    for i in userdata["data"]:
      if i["available"]:
        qualifications = i["qualifications"].split()
        if all(i in qualifications for i in new):
          output+=i["name"]+": "+i["username"]+"\n"
    if output!="":
      await message.channel.send(output)
    else:
      await message.channel.send("No one was found with that combination of tags.")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Inavalid command \nTry \n$help')
  else:
    raise error

@on_message.error
async def on_message_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Provide the required args')
        
bot.run(os.getenv('TOKEN'))

# import os
# import discord
# import json

# f = open("details.json")
# f1 = open("details2.json")

# data=json.load(f)
# userdata=json.load(f1)

# client=discord.Client()

# help="Usage: $start {TOPIC} \n\nHere are some of the available \n 1: Python\n 2: C++ \n 3: Java \n 4: Android \n 5: GSOC \n 6: Internship"


# @client.event
# async def on_ready():
#   print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   if message.content.startswith('$hello'):
#     await message.channel.send('Hello!')
    
#   if message.content.startswith('$help'):
#     await message.channel.send(help)
    
#   if message.content.startswith('$start'):
#     new=message.content.lower().split()
#     new=new[1:]
#     new.sort()
#     output = ""
#     for i in userdata["data"]:
#       if i["available"]:
#         qualifications = i["qualifications"].split()
#         if all(i in qualifications for i in new):
#           output+=i["name"]+": "+i["username"]+"\n"    

#     if output!="":
#       await message.channel.send(output)
#     else:
#       await message.channel.send("No one was found with that combination of tags.")
    
#   if message.content.startswith('$ping'):
#     await message.channel.send("David: <@293690940340699138>")
        
      

# client.run(os.getenv('TOKEN'))
    












'''bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 487258918465306634  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot'''

"""if lang in data.keys():
      #await message.channel.send(*data[lang])
      msg=""
      for i in data[lang]:
        msg+=i+" Qualifications: " +userdata[i.lower()]['qualifications']+"\n"
      await message.channel.send(msg)
      """