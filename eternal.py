import discord
from code import code_id
from discord.ext import commands

client = commands.Bot(command_prefix="!")
user = discord.Client()

@user.event
async def on_message(message):
    message.content.lower()
    if message.author == user.user: #brak reakcji na swoje akcje
        return

    if str(message.channel) == "meme" and message.content != "": #sekcja usuwania
        await message.channel.purge(limit=1)

    if message.content.startswith("sup") and str(message.channel) == "ogólny": #sekcja responsywności
        if str(message.author) == "SyriuszS#7555":
            await message.channel.send("Witaj " + str(message.author) + " mój twórco.")
        else:
            await message.channel.send("Jestem nowonarodzonym botem, naprawię Ci gust muzyczny <3")

user.run(code_id)
