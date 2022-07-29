from discord.ext import commands
import discord
import asyncio
import os


TOKEN = os.environ["TOKEN"]


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="m/",intents=intents,help_command=None,case_insensitive = True)



#on_ready
@bot.event
async def on_ready():
  print(f'login! {bot.user}')
  status_w = discord.Status.idle
  activtiy_w = discord.Activity(type=discord.ActivityType.playing,name="m/help")
  await bot.change_presence(activity=activtiy_w,status=status_w)

  

@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f'cogs.{extension}')
    loadokembed=discord.Embed(title="cog載入指令", description=f"載入 {extension} 完成", color=0x7FFFD4)
    loadokembed.set_footer(text=ctx.guild.name,icon_url=ctx.guild.icon)
    await ctx.send(embed=loadokembed)



@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension(f'cogs.{extension}')
    loadokembed=discord.Embed(title="cog載入指令", description=f"載入 {extension} 完成", color=0x7FFFD4)
    loadokembed.set_footer(text=ctx.guild.name,icon_url=ctx.guild.icon)
    await ctx.send(embed=loadokembed)



@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f'cogs.{extension}')
    loadokembed=discord.Embed(title="cog載入指令", description=f"載入 {extension} 完成", color=0x7FFFD4)
    loadokembed.set_footer(text=ctx.guild.name,icon_url=ctx.guild.icon)
    await ctx.send(embed=loadokembed)
    

@bot.event
async def on_member_join(member):
    if member.guild.id == 1002214825771933728:
        channel = bot.get_channel(1002384958935023737)
        guild = bot.get_guild(1002214825771933728)
        role = guild.get_role(1002221311084474459)
        await member.add_roles(role)
        embed = discord.Embed(title="成員加入",color=discord.Colour.random())
        embed.add_field(name=member.mention,value="加入了!")
        embed.set_footer(text=member.guild.name)
        await channel.send(embed=embed)
    elif member.guild.id == 1002384116483903558:
        guild = bot.get_guild(1002384116483903558)
        role = guild.get_role(1002221311084474459)
        await member.add_roles(role)
        channel = bot.get_channel(1002429031028883476)
        embed = discord.Embed(title="成員加入",color=discord.Colour.random())
        embed.add_field(name=member.mention,value="加入了!")
        embed.set_footer(text=member.guild.name)
        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    if member.guild.id == 1002214825771933728:
        channel = bot.get_channel(1002384958935023737)
        embed = discord.Embed(title="成員離開",color=discord.Colour.random())
        embed.add_field(name=member.mention,value="離開了!")
        embed.set_footer(text=member.guild.name)
        await channel.send(embed=embed)
    elif member.guild.id == 1002384116483903558:
        channel = bot.get_channel(1002429031028883476)
        embed = discord.Embed(title="成員離開",color=discord.Colour.random())
        embed.add_field(name=member,value="離開了!")
        embed.set_footer(text=member.guild.name)
        await channel.send(embed=embed)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")



async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())
