import discord
import youtube_dl
from code import code_id
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Poczekaj na koniec piosenki lub zatrzymaj komendą !hold")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Ogólne")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) #info tylko kiedy bot jest na kanale

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "144",
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command() #usunięcie bota z kanału
async def go_away(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()

@client.command()
async def hold(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nic jeszcze nie zostało puszczone...")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Żadna piosenka nie jest zatrzymana...")


client.run(code_id)
