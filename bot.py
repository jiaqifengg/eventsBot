import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="m!")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    print("-"*16)


@bot.command()
async def help(ctx, *args):
    pass


@bot.command()
async def event(ctx, *args):
    embed = discord.Embed(title="test", description="test", color=0xEFB3FF)
    await ctx.send(embed=embed)


bot.run(TOKEN)
