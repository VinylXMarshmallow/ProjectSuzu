import discord
import AI_test
import atexit
from datetime import datetime

from Tokens.DISCORD_KEY import DISCORD_KEY

DISCORD_TOKEN = DISCORD_KEY

intents = discord.Intents.all()

client = discord.Client(intents=intents)

history = []

@atexit.register
def goodbye():
    with open('log.txt', 'a') as the_file:
        the_file.write("\nOffline {0.user}\n")

@client.event
async def on_ready():
    with open('log.txt', 'a') as the_file:
        the_file.write("Online {0.user}\n".format(client))
    print("Online {0.user}".format(client))

@client.event
async def on_message(message):
    user = str(message.author).split('#')[0]
    user_message = str(message.content)


    if message.channel.name == 'chat-z-suzu':
        history.append([user,user_message])
        if len(history)>10:
            history.pop(0)
        if message.author == client.user:
            return
        await message.channel.send(AI_test.SendToOpenAI(history))
        now = datetime.now()
        current_time = now.strftime("%m/%d/%Y, %H:%M:%S\n")
        with open('AI_log.txt', 'a') as the_file:
            the_file.write(current_time)
            for content in history:
                the_file.write(content[0] + ": " + content[1] + "\n")
            the_file.write('\n')

    #nie odpowiadamy samemu sobie w pętli XDD
    if message.author == client.user:
        return

    return

client.run(DISCORD_TOKEN)
