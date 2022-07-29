import discord
from discord.ext import commands
import os
from message_commands import main_on_message
import functions_db
from dotenv import load_dotenv
from app import keep_alive
load_dotenv()

#IF IP TIME OUT/TEMP BAN -- TYPE "kill 1" IN THE SHELL

#Intents used for guild/member managment
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)



#TO GIVE 1 TO ALL NEW USERS FOR GRAND TOTAL OF WORDS
functions_db.hard_fix(client)


#displays message on console when logged in
@client.event
async def on_ready():
  print("Logged in as")
  print(client.user.name)
  print("------")


#reads all messages
main_on_message(client)


#uptime robot to keep bot alive
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN', None)
client.run(DISCORD_TOKEN)

keep_alive()