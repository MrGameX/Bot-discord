import discord
import asyncio
import random
import requests

prefix = "!"

client = discord.Client()
RTDid = "585508575057674250"
MrGameXid = "303933744971251713"

@client.event
async def on_ready():
    print("Logged in as.")
    print(client.user.name)
    print(client.user.id)
    print("-----")
    await client.change_presence(game=discord.Game(name="R6"))

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
       command = str(message.content[len(prefix):])
       if command.lower().startswith('ping'):
           msg = await client.send_message(message.channel, "pong")
           await client.delete_message(message)
           await asyncio.sleep(5)
           await client.delete_message(msg)

       elif command.lower().startswith('game') and "fondateur" in [y.name.lower() for y in message.author.roles]:
            game = message.content[6:]
            await client.change_presence(game=discord.Game(name=game))
            msg = await client.send_message(message.channel, "Le jeu à été changé par " + game)
            await asyncio.sleep(3)
            await client.delete_message(message)
            await asyncio.sleep(5)
            await client.delete_message(msg)


    elif message.content == "!pong":
        msg = await client.send_message(message.channel, "Hello, my friend")
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg)

    elif message.content == 'bite' or message.content == 'pd' or message.content == 'fuck':
        await client.delete_message(message)
        msg = await client.send_message(message.channel, 'Ce genre de message n\'est pas autorisé sur ce discord !')
        await asyncio.sleep(5)
        await client.delete_message(msg)


@client.event
async def on_member_join_(member):
    serverchannel = "585455247829237794"
    msg = "Hello, vous êtes sur le serveur de test !".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)


@client.event
async def on_member_remove(member):
    serveurchannel = "585455247829237794"
    msg = "Good bye".format(member.mention, member.server.name)
    await client.send_message(serveurchannel, msg)

client.run("NTg1NTA4NTc1MDU3Njc0MjUw.XPahxg.QoqaEfLqo11tE6mQ26ytAxX4WaU")
