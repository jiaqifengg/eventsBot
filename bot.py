import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client()


@client.event
async def on_message(msg):
    if msg.content == "hello" or msg.content == "hi":
        await msg.channel.send("hewwo~")


client.run(TOKEN)
