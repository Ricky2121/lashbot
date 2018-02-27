# Tutbot by Da532

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Hi I'm  Lash!")
    print ("I will be your personal assistant!")
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong! :ping_pong:")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("BOT'S STALKER")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="", description="So, you're probaby wondering, what are we and what do we do? Well, we provide a bot for everyone to use, free of charge! Meet Lash! He will be your bot, whenever you need him, he'll be sitting there, waiting for a special lash command! Get to know him more here ---> https://google.com", color=0x00ff00)
  
    embed.set_author(name="Meet Lash!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def version(ctx):
    await bot.say("I am running on version 0.1 Alpha")
    print ("version has been sent")

@bot.command(pass_context=True)
async def randomquote(ctx):
    await bot.say("Random quote")
    print ("version has been sent")





bot.run("NDE1MjUzMjQ1NjE5ODYzNTU0.DXOa8w.MsKFO5Zs-5XUEMTkZsiKA1INjyM")