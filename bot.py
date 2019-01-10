import random
import discord
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('!')
TOKEN = "XXXXSECRET_TOKENXXXXXXX"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix='rb?')
 
@client.command(pass_context=True)
async def bc(ctx, *, message):
    channel = client.get_channel("513798181558157362")
    await client.send_message(channel, message)
    await client.say("Message Was Sent :+1:")
    print ("Bot Just Broadcasted A Message")

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)
    await client.say("Member Was Kicked :+1:")
    
@bot.command(pass_context=True)
async def tf1(ctx):
    embed=discord.Embed(title="Test", description="1", color=0x5bcdee)
    embed.set_footer(text="Test2")
    await bot.say(discord.Object(id='456277299189383168'),  embed=embed)
    
@client.command()
async def echo(content):
	await client.say(content)

@client.command(pass_context=True)
async def test(ctx):
    await client.say('testing')
    await client.edit.message('Ragebot')

@client.command()
async def developers():
	await client.say('My Developer Is -> **✘-Oyt-ⱽᵉʳⁱᶠy✘#8779**')
	print ("Bot Info About Developers")
	
@client.command(pass_context=True)
async def invite(ctx):
	await client.say("Invite Me With That Link")
	await client.say("https://discordapp.com/oauth2/authorize?client_id=518815819124441089&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize&response_type=code&scope=guilds%20guilds.join%20bot")
	print ("Bot Sent Invite Link")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with Rage Bot Central™"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run("NTE4ODE1ODE5MTI0NDQxMDg5.DuWvBQ.KQOFle-ANh15BDWy4_hRcsh2JzM")
