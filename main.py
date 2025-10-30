import discord
from discord.ext import commands
import clashAPI

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    assert bot.user is not None
    await bot.tree.sync()
    print(f"Logged on as {bot.user}\n")

@bot.tree.command(name="mt-lookup", description="Merge Tactics lookup")
async def lookup(interaction: discord.Interaction, tag: str):
    data = clashAPI.getPlayerData(tag)
    try:
        if data.status_code != 200:
            error = data.status_code
            await interaction.response.send_message(f"Error {error}")
    except AttributeError:
        mergeTac = data["progress"]["AutoChess_2025_Nov"]
        textToSend = ("**--Merge Tactics--**\n"
                        f"Username: {data["name"]}\n"
                        f"Current Rank: {mergeTac["arena"]["name"]}\n"
                        f"Highest Trophies: {mergeTac["bestTrophies"]}\n"
                        f"Current Trophies: {mergeTac["trophies"]}")
        await interaction.response.send_message(textToSend)

@bot.tree.command(name="mt-top10k", description="Gets the player at no.10k")
async def top10k(interaction: discord.Interaction):
    data = clashAPI.getTop10k()
    try:
        items = data["items"][0]
        textToSend = ("**The person at rank 10,000 is:**\n"
                    f"Username: {items["name"]}\n"
                    f"Trophies: {items["score"]}")
        await interaction.response.send_message(textToSend)
    except:
        await interaction.response.send_message("An error has occured")

@bot.tree.command(name="cr-2v2test", description="Testing for 2v2 Clash Royale")
async def doublesTest(interaction: discord.Interaction, tag: str):
    pass

bot.run(BOT_TOKEN)
