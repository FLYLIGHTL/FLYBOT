import discord
import os
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

    if message.content.startswith("?attention"):
        sentence=message.content.split(" ")
    await client.send_message(message.channel, "ATTENTION!\n\n"+"**"+str(sentence[1])+"**")


    if message.content.startswith("?version"):
        await client.send_message(message.channel, "**FLYBOT V0.1(Beta)**")


access_token=os.environ["BOT_TOKEN"]        
client.run(access_token)

