import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import eventhandler
import random

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="m!")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    print("-" * 16)


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help",
                       description="Use m!help <command> for more details",
                       color=random.randint(0, 0xFFFFFF))

    em.add_field(name="event", value="giveaway, event, secret santa")
    em.add_field(name="music", value="play,stop,continue,clear,queue")

    await ctx.send(embed=em)


@help.command()
async def event(ctx):
    em = discord.Embed(title="General Event",
                       description="Create any event online or not")
    em.add_field(name="Syntax", value="m!event - create an event interactively"
                                      "\n(must have the Manage Server permission)")
    await ctx.send(embed=em)


@bot.command()
async def event(ctx, *args):
    description = ""
    options = ["event", "giveaway", "secretsanta"]
    error = f"Usage: m!event <{', '.join(i for i in options)}>"

    user = ctx.message.author

    # check if there are args and if they are correct or not
    if len(args) == 0 or args[0] not in options:
        description = error

    else:
        # event : title, description, time, and place
        if args[0] == options[0]:
            eventhandler.event(user)
        # giveaway : title, end of giveaway, award
        elif args[0] == options[1]:
            eventhandler.giveaway(user)
        # secret santa : time, place, budget, participants, save group(?), accept by
        elif args[0] == options[2]:
            eventhandler.secretsanta(user)

    embed = discord.Embed(title="Event", description=description, color=0xEFB3FF)

    await ctx.send(embed=embed)
bot.run(TOKEN)
