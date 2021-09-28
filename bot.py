import os 
import discord
from discord import client
from discord.ext import commands
import aiohttp
import time

TOKEN = " " 


bot = commands.Bot(command_prefix= ">>", help_command=None)

@bot.command(name = "ping")
async def ping(ctx):
  await ctx.reply("pong")



@bot.command(name="dog")
async def dog(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get('https://some-random-api.ml/img/dog')
    dogjson = await request.json() # This time we'll get the fact request as well! 
    request2 = await session.get('https://some-random-api.ml/facts/dog')
    factjson = await request2.json()
  embedog = discord.Embed(title="Dog!", color=discord.Color.red())
  embedog.set_image(url=dogjson['link'])
  embedog.set_footer(text=factjson['fact'])
  await ctx.send(embed=embedog)
  
  
@bot.command(name = "embed")
async def embed(ctx, channel: discord.TextChannel, *, message):
  if ctx.message.author.id == 562028317666967573:
    embed = discord.Embed(title="Erradics Shop", color = discord.Color.red(), description = message)
    embed.set_footer(text = "By Nugget")
    await channel.send(embed = embed)
    await ctx.reply("Enviado.")
    
  if ctx.message.author.id != 562028317666967573:
    await ctx.reply("No tienes permiso para este comando.")


  
@bot.command(name = "embed2")
async def embed2(ctx, channel: discord.TextChannel,imagen, *, message):
  if ctx.message.author.id == 562028317666967573:
    embedd = discord.Embed(title="Erradics Shop", color = discord.Color.red(), description = message)
    embedd.set_image(url = imagen)
    embedd.set_footer(text = "By Nugget")
    await channel.send(embed = embedd)
    await ctx.reply("Enviado.")
    
  if ctx.message.author.id != 562028317666967573:
    await ctx.reply("No tienes permiso para este comando.")










@bot.command(name = "desc")
async def desc(ctx, *,xd):
  if ctx.message.author.id == 562028317666967573:
    await bot.change_presence(activity=discord.Game(name=xd))
    await ctx.reply("Descripción cambiada.")
    
  if ctx.message.author.id != 562028317666967573:
    await ctx.reply("No tienes permiso para este comando.")






@bot.command(pass_context=True)
async def say(ctx, channel: discord.TextChannel, *, messagee):

      if ctx.message.author.id == 562028317666967573:
        await channel.send(messagee)
        await ctx.send("Enviado.")
        print(messagee)



      if ctx.message.author.id != 562028317666967573:
        print("no perms")
        await ctx.reply("No tienes permiso para usar este comando.")

   
@bot.event
async def on_raw_reaction_add(payload):
  if str(payload.emoji) == "📩":
    guild = bot.get_guild(payload.guild_id) 
    
    channel = await guild.create_text_channel("Ticket")
    return channel


@bot.event
async def on_ready():
  print("Bot is ready!")
  await  bot.change_presence(activity=discord.Game(name="Erradics Shop."))   
  
  
  
    

  
  
  
  
bot.run(TOKEN)
