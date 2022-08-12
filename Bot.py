import discord
from discord.ext import commands

TOKEN = 'Your Bot Token Here'

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('Bot Is Ready!')


@client.command()
async def ping(ctx):
    embed = discord.Embed(
        description=(
            f'Pong!'),
        colour=discord.Colour.purple()
    )
    await ctx.send(embed=embed)

client.run(TOKEN)
