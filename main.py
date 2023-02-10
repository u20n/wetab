import discord, sys
from discord import FFmpegPCMAudio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='>', intents=intents)

is_connected = lambda guild : discord.utils.get(bot.voice_clients, guild=guild)

@bot.command()
async def join(ctx):
    if is_connected(ctx.guild) == None: 
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send(f"+{ctx.message.author.voice.channel}")
        vc.play(FFmpegPCMAudio("https://playerservices.streamtheworld.com/api/livestream-redirect/WETAFM.mp3"))

@bot.command()
async def leave(ctx):
    if is_connected(ctx.guild): 
        await ctx.send(f"-{ctx.message.author.voice.channel}")
        ctx.guild.voice_client.stop()
        await ctx.guild.voice_client.disconnect()

bot.run(sys.argv[1])
