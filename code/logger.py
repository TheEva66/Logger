import discord
from discord.ext import commands
from discord.ext import commands
from colorama import Fore, Style
import time
import asyncio
import requests
import subprocess
#verification cehck from a pastebin using a hwid
def check():
    global lol
    global hwid
    res = 4

    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('https://pastebin.com/3pZv91nK') # Paste your URL  e.g(https://pastebin.com)

    try:
        check = r.text
        if hwid in check:
            res = 1
            pass
        else:
            res = 0
    except:
        
        print("[ERROR] Failed to connect to database")
        time.sleep(5)  
        res = 2
    
    lol = 2
    return res
res = (check())
if res == 0:
    print(f"""YOU ARE NOT AUTHORIZED
if this is a mistake send this string to -insert name here-#0001

{hwid}""")
    time.sleep(60)
    quit()
elif res == 1:
    print("authenticated")
else:
    print("database error please try again later")
    time.sleep(30)
    quit()

L = open("TOKEN.txt", "+a")
L.close
#creates / checks to see if TOKEN.txt has anything in it
def emptitiy(file_name):
    """ Check if file is empty by reading first character in it"""
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False
empty_file = emptitiy("TOKEN.txt")
if empty_file == True:
    print("Put your user token in TOKEN.txt")
    time.sleep(30)
    quit()
L = open("TOKEN.txt")
Token = L.read()
#discord intents dont matter for self bots
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.presences = True
client = commands.Bot(command_prefix="!",intents = intents, self_bot = True)
#on ready command
@client.event
async def on_ready():
    print(f"{client.user} is logged on")
#checks for warnings and sends/logs them in a txt file
@client.command()
async def w(ctx, *, name: str):
    channel = client.get_channel(960730940362080256)
    messages = await channel.history(limit=1000).flatten()
    f = open("warnings.txt", "a+")
    f.write(f"\n ------------------warns for {name}--------------")
    await ctx.send(f"""------------WARNS FOR {name}------------
    
    
    """)
    for msg in messages:
        if name in msg.content:
            await ctx.send(msg.content)
            f.write(f"{msg.content} \n")
    f.close
#logs warnings in tje discord
@client.command()
async def log(ctx, *, name: str):
    await ctx.send("What is the reason for logging")
    await asyncio.sleep(1)
    def check(m): return m.author == ctx.author and m.channel == ctx.channel
    reason = await client.wait_for('message', check=check, timeout=None)
    await ctx.send("what is the punishment given")
    await asyncio.sleep(1)
    def check(m): return m.author == ctx.author and m.channel == ctx.channel

    punish = await client.wait_for('message', check=check, timeout=None)
    if punish is None:
        await ctx.send("message timeout (i gave you 5 minutes :facepalm:)")
        return
    await ctx.send(f"{name} has been logged for {reason.content} punishment {punish.content}")
    channel = client.get_channel(960730940362080256)
    await channel.send(f"{name} {reason.content} {punish.content}")


client.run(Token, bot = False)