import discord
import asyncio
import random
client = discord.Client()


@client.event
async def on_ready():
    print("Login Bot")
    print(client.user.name)
    print(client.user.id)
    print("-------------")
    await client.change_presence(game=discord.Game(name='FLYBOT',type=1))


@client.event
async def on_message(message):
    if message.content.startswith("?hello"):
        await client.send_message(message.channel, "**안녕하세요**")

    if message.content.startswith("?help"):
        await client.send_message(message.channel, "FLYBOT의 명령어 목록입니다!\n?hello : 인사를 나누는 명령어\n?dice : 주사위를 던지는 명령어\n?attention _sentence_ : _sentence_를 강조해 출력하는 명령어\n?Version : 현재 FLYBOT의 버전을 알려주는 명령어")

    if message.content.startswith("?dice"):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        for i in range(1, rolld[0]+1):
            dice = dice + random.randint(1, rolld[1])
        await client.send_message(message.channel, str(dice))

    if message.content.startswith("?attention"):
        sentence=message.content.split(" ")
    await client.send_message(message.channel, "ATTENTION!\n\n"+"**"+str(sentence[1])+"**")


    if message.content.startswith("?version"):
        await client.send_message(message.channel, "**FLYBOT V0.1(Beta)**")


client.run('NTQ1NTAwODM2MTgxMzExNDg4.D0aldw.mXz8yE5RRiMofMZD__Pc8ZRwbI8')