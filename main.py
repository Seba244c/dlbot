import discord
from discord.ext import commands
import os
from tok import tok

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$',intents=intents)

@client.command()
async def test(ctx):
    await ctx.send("Downloading all...")
    messages = [message async for message in ctx.channel.history(limit=200)]
    await ctx.send(str(len(messages)) + " messages")
    attachments = []
    for message in messages:
        attachments += message.attachments
    
    await ctx.send(str(len(attachments)) + " attachments")
    
    amm = len(attachments)
    i = 0
    pp = max(0.05,1/amm)
    percent = pp

    for attachment in attachments:
        i += 1
        await attachment.save("download/"+str(i*38749)+attachment.filename)
        if amm   / i > percent:
            await ctx.send(str(percent*100) + "%")
            percent += pp
    await ctx.send("Done! (100%)")
    
print(tok)
client.run(tok)
