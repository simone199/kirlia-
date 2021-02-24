from discord.ext.commands import Bot
import discord, chalk
from PIL import Image
from io import BytesIO
import asyncio
import logging
import random
from discord.voice_client import VoiceClient
from random import choice
import os
from discord import utils
from itertools import cycle
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import json, requests
from flask import Flask
from threading import Thread
import keep_alive
import shutil
from os import system
import youtube_dl
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext import (commands, tasks)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from colorama import Fore
from sys import platform
from PIL import Image
from gtts import gTTS
import sqlite3
from sys import argv
import pathlib
import json
import sys
import os
from itertools import cycle
import configparser
from discord import Spotify
import sys
import typing
import ffmpeg
from discord.ext.commands import CommandNotFound
from discord import guild
client = commands.Bot(command_prefix="k/")

config = configparser.ConfigParser()
print(id)
config.read('config.ini')
client.remove_command("help")
status = config.get("Status", "sta")
stato = cycle(["k/help | shows the command list", status])

file = "config.ini"
config.read(file)

# task iniziali!
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    change_status.start()
    guilds = client.guilds
    nome = guilds[0]
    print(f'Loggato come:\n{client.user.name}\n{client.user.id}')


# cogs load
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")






# status automatico
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(stato)))






@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')










@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


@client.command()
async def help(ctx):
    page1 = discord.Embed(
        title="<:staffer:804739976272674816>page1/1 (Moderation Commands)<:staffer:804739976272674816>"
        "",
        description=""
       "`k/Ban @User (reason) = [Mod] Ban a user from the server;`\n"
       "`k/UnBan @User  = [Mod]  unBan a user from the server;`\n"
       "`k/mute @User (reason)  = [Mod]  mute a user from the server;`\n"
       "`k/unmute @User  = [Mod]  unmute a user from the server;`\n"
       "`k/clear (N)  = [Mod]  delete messages in a channel;`\n"
       "`k/lockdown (ChannelID)  = [Mod]  Lock a server channel;`\n"
       "`k/unlock (ChannelID)  = [Mod]  unlock a server channel;`\n"
       "`k/addrole @user (ID role)   = [Mod]  give someone a role;`\n"
       "`k/removerole @user (ID role) =   [Mod]  take someone out of a role;`\n"
       "`k/createrole  (RoleName)  =  [Mod]  create a role;`\n"
       "`k/slowmode  (Channel)  =  [Mod]  set slow chat;`\n"
       "`k/nick  @User   = [Mod]  set the nickname on the server to someone;`\n"              
       "`k/chat  (Channel)   = [Mod]  export a channel chat;`\n"
       "`k/editrole (RoleID)   = [Mod]  change color and edit a role;`\n"
       "`k/delchannel (ID)   = [Mod]  delete and recreate a channel;`\n"
       "`k/warn @User   = [Mod]  warn a user from the server;`\n"
       "`k/warnlist @User   = [Mod]  show user warns;`\n"
       "`k/delwarn @User   = [Mod]  delete a user specific warn;`\n"
       "`k/delwarnid (ID)   = [Mod]  delete a user specific warn ID;`\n"
       "`k/clearwarn @User   = [Mod]  delete all warns of a user;`\n"
       "`k/clearwarn (ID)   = [Mod]  delete all warns of a user ID;`\n"
       "`k/kick @User   = [Mod]   kick a user off the server;`\n"
       "`k/tempmute  = @User (Reason)   [Mod] time mutes a user from the server;`\n",
        colour=discord.Colour.blue())
    page2 = discord.Embed(
        title="<:sparkles_blurple:792923730795429899>page2/2 (Funny commands)<:sparkles_blurple:792923730795429899>"
        "",
        description=""
        "` k/slot  =  Play Slot Machines;`\n"
        "` k/lyonwgf @User =  becomes a real lion;`\n"
        "` k/kiss @User =  Give Someone A Kiss;`\n"
        "` k/pat @User =  Give Someone A Caress;`\n"
        "` k/hug @User =  Give A Hug To Someone;`\n"
        "` k/slap @User =  Give Someone A Slap;`\n"
        "` k/cry @User =  You Cry;`\n"
        "` k/cute @User =  You Cute;`\n"
        "` k/dance @User =  You Dance;`\n"
        "` k/fox =  Send Pictures Of Foxes;`\n"
        "` k/dog =  Send Pictures Of Dogs;`\n"
        "` k/combine =  (text) Make A Combination Of 2 Names;`\n"
        "` k/meme =  Send Random Memes;`\n"
        "` k/anime =  Send Random Souls;`\n"
        "` k/rolldice =  Send Random Roll;`\n"
        "` k/8ball = (text) Have The Bot Send A Response;`\n",
        colour=discord.Colour.blue())
    page3 = discord.Embed(
        title="<:robit:804815877497159741>page3/3 (Utility Commands)<:robit:804815877497159741>"
        "",
        description=""
        "` k/invite =   Send Bot Invitation;`\n"
        "` k/userinfo =  @User Send User Information;`\n"
        "` k/serverinfo =  Send Server Informationr;`\n"
        "` k/ping =  Show the Ping of the Bot;`\n"
        "` k/avatar =  @User Show Avatar Of A User;`\n"
        "` k/revav =  @User Search For A User Avatar On Google;`\n"
        "` k/say = (message) Have The Bot Send a Message;`\n"
        "` k/poll (q1, q2, Time) =  Create A Survey;`\n"
        "` k/dm (Dm) =  Send A Message To  Message;`\n"
        "` k/infobot =  Show Bot Information;`\n",
        colour=discord.Colour.blue())

    pages = [page1, page2, page3]

    message = await ctx.send(embed=page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed=pages[i])

        try:
            reaction, user = await client.wait_for(
                'reaction_add', timeout=30.0, check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(
        f'<:safy:792867515411595285>**Security Guard** The Nickname Was Changed For {member.mention} '
    )




@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you do not have permission to set the nickname",
        )
        await ctx.send(embed=embed)




#clear Cancella dei messagi


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(
        ctx,
        number,
):
    member = ctx.message.author
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=int(number)):
        messages.append(message)
    await channel.delete_messages(messages)
    await channel.send(
        "<:safy:792867515411595285>**Security Guard** Deleted Messages")



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to delete messages",
        )
        await ctx.send(embed=embed)








#ping mostra in ping del Bot


@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(
        title=None,
        description=
        '<a:8527_discord_loading:792922560387874836> Ping of **Kirlia**   {}'.
        format(round((t2 - t1) * 1000)),
        color=0x3498db)
    await channel.send(embed=embed)


#userinfo mostar le info di un utente di discord


@client.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(
        colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(
        text=f"Command Executed By {ctx.author}",
        icon_url=ctx.author.avatar_url)

    embed.add_field(
        name="<a:right:792578459750760498>**ID:**", value=member.id)
    embed.add_field(
        name="<a:right:792578459750760498>**Username:**",
        value=member.display_name)

    embed.add_field(
        name="<a:right:792578459750760498>**Account Created**",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="<a:right:792578459750760498>**Entered The Server**",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(
        name=f"<a:right:792578459750760498>**Roles** ({len(roles)})",
        value=" ".join([role.mention for role in roles]))
    embed.add_field(
        name="<a:right:792578459750760498>**High Roles**",
        value=member.top_role.mention)
    embed.add_field(
        name=" <a:right:792578459750760498> **It's A Bot ?**",
        value=member.bot)
    await ctx.send(embed=embed)

 




#manda invito del Bot



@client.command(pass_context=True)
async def invite(ctx):
    user = ctx.author
    embed = discord.Embed(
        title=
        "**<a:yee:793612949679636502>Bot Invitation<a:yee:793612949679636502>**",
        description=
        " <a:redd:805116638927781888> `Invite Me` **[Click Me](https://discord.com/oauth2/authorize?client_id=788532430642348062&scope=bot&permissions=2147352511)**\n",
        colour=discord.Colour.blue())

    await ctx.send(embed=embed)






#mostra le info di Un Server Discord


@client.command()
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f"<a:right:792578459750760498>Server Information {guild}", description="", timestamp = ctx.message.created_at, color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="<a:right:792578459750760498>**Owner**", value=guild.owner, inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Server created**:", value=guild.created_at, inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Description**:", value= guild.description, inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Member Count**:", value= guild.member_count, inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Channel Count**:", value= len(guild.channels), inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Role Count**:", value=len(guild.roles), inline=True)
    embed.add_field(name="<a:right:792578459750760498>**Number Boost**:", value= guild.premium_subscription_count, inline=False)
    embed.add_field(name="<a:right:792578459750760498>**Emoji:**", value=guild.emoji_limit, inline=True)
    embed.add_field(name='<a:right:792578459750760498>**Verification Level**', value=str(ctx.guild.verification_level), inline=False)
    embed.set_footer(text=f"Command executed by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)
 
  
  

 

    #mostra avatar di un utente discord


@client.command()
async def avatar(ctx, member: discord.Member = True):
    asyncio.sleep(5)
    if not member:
        member = ctx.message.author
    embed = discord.Embed(color=0x3498db)
    embed.title = "<a:5843_URL:792578730572120106> User Avatar"
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@avatar.error
async def   avatar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="Please Mention Someone To Execute The Command Or Make Sure You Have Written The Command Well",
        )
        await ctx.send(embed=embed)



#fai una domanda a un bot


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    embed = discord.Embed(color=0x3498db)
    responses = [
        '  **<:info:791489284855169075> Probably** ',
        '   **<:info:791489284855169075> Probably Not** ',
    ]
    await ctx.send(
        f'<:question:791650160274440212> **Question**: {question}\nResponse{random.choice(responses)}'
    )



@_8ball.error
async def  _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)

#gioca alle slot-machine


@client.command(aliases=['slots', 'bet'])
async def slot(ctx):  # b'\xfc'
    asyncio.sleep(2)
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(
            embed=discord.Embed.from_dict({
                "title":
                " Slot machine",
                "description":
                f"{slotmachine}<a:yess:791711775057379328>All Matches, You Won!"
            }))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(
            embed=discord.Embed.from_dict({
                "title":
                "Slot machine",
                "description":
                f"{slotmachine}<a:yess:791711775057379328> 2 In A Row, You Win!"
            }))
    else:
        await ctx.send(
            embed=discord.Embed.from_dict({
                "title":
                "Slot Machine",
                "description":
                f"{slotmachine}<a:nope:791711739846590494> You Lost"
            }))


#mostra  Del infobot





#Comando diventa Layon Wgf


@client.command()
async def lyonwgf(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    lyonwgf = Image.open("lyonwgf.jpg")

    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((501, 500))

    lyonwgf.paste(pfp, (600, 46))

    lyonwgf.save("profile.jpg")

    await ctx.send(file=discord.File("profile.jpg"))



@lyonwgf.error
async def  lyonwgf_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(
        f"<:safy:792867515411595285>**Security Guard** Set The Slowmode Delay In This Channel To {seconds} Seconds"
    )



@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to slow chat",
        )
        await ctx.send(embed=embed)



@client.command(description="Mutes The Specified User.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(
                mutedRole,
                speak=False,
                send_messages=False,
                read_message_history=True,
                read_messages=False)
    embed = discord.Embed(
        title="<:safy:792867515411595285>**Security Guard** ",
        description=
        f"{member.mention}<:police:795372543329566770> Muted User ",
        colour=discord.Colour.blue())
    embed.add_field(
        name=" <:headr:795372543032164412> Reason",
        value=reason,
        inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(
        f"<:police:795372543329566770> You'Ve Been Muted {guild.name}  <:headr:795372543032164412> Reason {reason}"
    )


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to mute",
        )
        await ctx.send(embed=embed)





@client.command(description="Unmutes A Specified User")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(
        f"  <:police:795372543329566770>  You Have Been Unmuted {ctx.guild.name}"
    )
    embed = discord.Embed(
        title="<:safy:792867515411595285>**Security Guard**",
        description=
        f" <:headr:795372543032164412> User Unmute {member.mention}",
        colour=discord.Colour.blue())
    await ctx.send(embed=embed)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to unmute",
        )
        await ctx.send(embed=embed)





@client.command()
@commands.has_permissions(manage_messages=True)
async def dm(ctx, member: discord.Member, *, message):
    embed = discord.Embed(
        title=message,
        description=f"<a:discordblob:792923661581025292> Dm From {ctx.author}",
        colour=discord.Color.blue())

    await member.send(embed=embed)


@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to have the bot send private messages",
        )
        await ctx.send(embed=embed)


# comando cerca su google un avatar utente


@client.command()
async def revav(ctx, user: discord.Member = None):  # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(
            description=
            f" Avatar Profile Found On Google <a:google:793613970749390869> https://images.google.com/searchbyimage?image_url={user.avatar_url}"
        )
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)



@revav.error
async def  revav_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)


# comando fai una combinazione di due nomi parole


@client.command()
async def combine(ctx, name1, name2):  # b'\xfc'
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@combine.error
async def  combine_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)



#manda foto di cani


@client.command()
async def dog(ctx):  # b'\xfc'
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))


#manda foto di volpi


@client.command()
async def fox(ctx):  # b'\xfc'
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="!who", color=0x3498db)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])


@client.command()
async def slap(ctx, user: discord.Member):  # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@slap.error
async def  slap_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)

@client.command()
async def hug(ctx, user: discord.Member):  # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.name)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)





@hug.error
async def  hug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)





@client.command()
async def pat(ctx, user: discord.Member):  # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.name)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@pat.error
async def  pat_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)




@client.command()
async def kiss(ctx, user: discord.Member):  # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.name)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@kiss.error
async def  kiss_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)



@client.command()
async def meme(ctx):
    choices = [
        "https://imgur.com/a/MvYabuk",
        "https://imgur.com/a/cKEp545",
        "https://imgur.com/a/5D4XVLl",
        "https://imgur.com/a/6IioFXt",
        "https://imgur.com/a/KdVz4WE",
        "https://imgur.com/a/BlLPvvc",
        "https://imgur.com/a/aKEMcfO",
        "https://imgur.com/a/e7Mnu9t",
        "https://imgur.com/a/sVfVodl",
        "https://imgur.com/a/F9Zz4A0",
        "https://imgur.com/a/vbCDxww",
        "https://imgur.com/a/3K0AHR3",
        "https://imgur.com/gallery/yJo4w",
        "https://imgur.com/gallery/asKtMan",
    ]
    ranmeme = random.choice(choices)
    await ctx.send(ranmeme)





@client.command(pass_context=True)
async def lockdown(ctx, channel: discord.TextChannel):
    the_channel = client.get_channel(channel.id)
    await the_channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(title="<:safy:792867515411595285>**Security Guard** Blocked Channel", color=0x3498db)
    await channel.send(embed=embed)




@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to block the channel",
        )
        await ctx.send(embed=embed)






@client.command(pass_context=True)
async def unlock(ctx, channel: discord.TextChannel):
    the_channel = client.get_channel(channel.id)
    await the_channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = discord.Embed(title="<:safy:792867515411595285>**Security Guard** Channel Unlocked", color=0x3498db)
    await channel.send(embed=embed)




@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permission to unblock the channel",
        )
        await ctx.send(embed=embed)






#say command


@client.command()
async def say(ctx, *, words):
    em = discord.Embed(color=0x3498db)
    em.add_field(name=f" {ctx.author}" , value=f"{words}".format(words))
    await ctx.send(embed=em)


@say.error
async def  say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)


#addrole command


@client.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(
        f"<:safy:792867515411595285>**Security Guard** {ctx.author.name}, {user.name} Has Given Role ID Role {role.id}"
    )



@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" you don't have permissions to add roles",
        )
        await ctx.send(embed=embed)



@client.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(
        f"<:safy:792867515411595285>**Security Guard** {ctx.author.name}, {user.name} Removed a Role ID Role {role.id}"
    )


@removerole.error
async def removerole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you do not have the permissions to remove the roles",
        )
        await ctx.send(embed=embed)


@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, *, name):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.send(
        f'<:safy:792867515411595285>**Security Guard** The Role `{name}` Was created'
    )


@createrole.error
async def createrole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permissions to create roles",
        )
        await ctx.send(embed=embed)











@client.command()
@commands.has_permissions(administrator=True)
async def chat(ctx):
    with open("file.txt", "w") as file:
        async for message in ctx.history(limit=1000):
            file.write(str(message.content + "\n"))

    with open("file.txt", "rb") as file:
        await ctx.send(
            " <a:verifiedd:791463680855900161> **Exported Chat**",
            file=discord.File(file, "chat.txt"))
    await ctx.send(" <:safy:792867515411595285>**Security Guard** **Done!**")

@chat.error
async def chat_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to export channel chat",
        )
        await ctx.send(embed=embed)







@client.command()
async def anime(ctx):
    choices = [
        "https://imgur.com/gallery/N89w0",
        "https://imgur.com/gallery/dtYTe",
        "https://imgur.com/gallery/4gWrs",
        "https://imgur.com/gallery/2xfG6",
        "https://imgur.com/gallery/van3M",
        "https://imgur.com/gallery/HgtMG",
        "https://imgur.com/gallery/PJBNl",
        "https://imgur.com/gallery/JmMu5",
        "https://imgur.com/gallery/eKuGn",
        "https://imgur.com/gallery/fDHCg",
    ]
    ranmeme = random.choice(choices)
    await ctx.send(ranmeme)


@client.command()
async def rolldice(ctx):
    time.sleep(2)
    dice4 = ["1", "2", "3", "4"]
    dice6 = ["1", "2", "3", "4", "5", "6"]
    dice8 = ["1", "2", "3", "4", "5", "6", "7", "8"]
    dice10 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    dice12 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    dice20 = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
        "14", "15", "16", "17", "18", "19", "20"
    ]

    message = await ctx.send(
        "Choose a number:\n**4**, **6**, **8**, **10**, **12**, **20** ")

    def check4(m):
        return m.author == ctx.author and m.content == "4"

    try:
        await client.wait_for('message', check=check4, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice4)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn't Answer In **30** Second!"
        )

    def check6(m):
        return m.author == ctx.author and m.content == "6"

    try:
        await client.wait_for('message', check=check6, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice6)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn'T Answer In **30** Second!"
        )

    def check8(m):
        return m.author == ctx.author and m.content == "8"

    try:
        await client.wait_for('message', check=check8, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice8)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn'T Answer In **30** Second!"
        )

    def check10(m):
        return m.author == ctx.author and m.content == "10"

    try:
        await client.wait_for('message', check=check10, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice10)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn'T Answer In **30** Second!"
        )

    def check12(m):
        return m.author == ctx.author and m.content == "12"

    try:
        await client.wait_for('message', check=check12, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice12)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn'T Answer In **30** Second!"
        )

    def check20(m):
        return m.author == ctx.author and m.content == "20"

    try:
        await client.wait_for('message', check=check20, timeout=30.0)
        coming = await ctx.send("Here it comes...")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.choice(dice20)}**")

    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(
            "Procces Has Been Canceled Because You Didn'T Answer In **30** Second!"
        )




@client.command()
@commands.is_owner()
@commands.has_permissions(administrator=True)
async def delchannel(ctx, channel_id):
    channel_id = int(''.join(i for i in channel_id if i.isdigit())) 
    existing_channel = client.get_channel(channel_id)
    if existing_channel:
        await existing_channel.clone(reason="<:safy:792867515411595285>**Security Guard** Channel Deleted")
        await existing_channel.delete()
    else:
        await ctx.send(f'<:safy:792867515411595285>**Security Guard** No Channel Named **{channel_id}** Was Found')
        

@delchannel.error
async def delchannel_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="You don't have enough permissions to delete the channel",
        )
        await ctx.send(embed=embed)





        

@client.command()
@commands.is_owner()
async def editrole(ctx, role_id: discord.Role, colour: discord.Colour, *, name = None):
    await role_id.edit(colour = colour)
    if name != None:
        await role_id.edit(name = name)

    embed = discord.Embed(
        description = (f'<:safy:792867515411595285>**Security Guard** The Changes For Role {role_id} have been Applied.'),
        colour = colour
    ) 
    await ctx.send(embed=embed)



@editrole.error
async def editrole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you do not have permission to change the role you must be the founder of the server",
        )
        await ctx.send(embed=embed)


@client.command()
async def cry(ctx, user: discord.Member = None):  # b'\xfc'
        num = random.randrange(1, 6)
        a = {1: "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
             2: "http://giphygifs.s3.amazonaws.com/media/mvRwcoCJ9kGTS/giphy.gif",
             3: "https://66.media.tumblr.com/5b4e0848d8080db04dbfedf31a4869e2/tumblr_inline_or4whcrg1z1ueut6r_540.gif",
             4: "http://giphygifs.s3.amazonaws.com/media/8YutMatqkTfSE/giphy.gif",
             5: "https://media.giphy.com/media/ZlWplgoWyskQo/giphy.gif",
             6: "https://media2.giphy.com/media/jxbzLNeT18a3K/giphy.gif"}
        gif = a[num]

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Cry", value=f"{ctx.author.mention} Is sad")
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

@cry.error
async def  cry_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)


@client.command()
async def cute(ctx, user: discord.Member):  # b'\xfc'
        num = random.randrange(1, 6)
        a = {1: "https://media.giphy.com/media/4CgLWhKNYdQNq/giphy.gif",
             2: "https://media.giphy.com/media/lHTTeBRVbwqGs/giphy.gif",
             3: "https://media.giphy.com/media/IzjJJK2UMugWA/giphy.gif",
             4: "https://media.giphy.com/media/M68ca96XBQiCQ/giphy.gif",
             5: "https://media.giphy.com/media/VpcYdQpElriNy/giphy.gif",
             6: "https://media.giphy.com/media/BP9fPzjwjJlUk/giphy.gif"}
        gif = a[num]

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="cute", value=f"{ctx.author.mention} is Cute")
        embed.set_image(url=gif)
        await ctx.send(embed=embed)


@cute.error
async def  cute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)


@client.command()
async def dance(ctx, user: discord.Member = None):  # b'\xfc'
        num = random.randrange(1, 6)
        a = {1: "https://media.giphy.com/media/HZboJ5Pkti9k4/giphy.gif",
             2: "https://media.giphy.com/media/ss9NqmOeQxRKg/giphy.gif",
             3: "https://media.giphy.com/media/ss9NqmOeQxRKg/giphy.gif",
             4: "https://media.giphy.com/media/b7l5cvG94cqo8/giphy.gif",
             5: "https://media.giphy.com/media/jCaU8WfesJfH2/giphy.gif",
             6: "https://media.giphy.com/media/k7J8aS3xpmhpK/giphy.gif"}
        gif = a[num]

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Dance", value=f"{ctx.author.mention} is dancing")
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

@dance.error
async def  dance_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)



@client.command(name='infobot')
async def infobot(ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.title = 'Bot Info'
    em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    try:
        em.description = client.psa + '\n[Support Server](https://discord.gg/xZSpZdaRpG)'
    except AttributeError:
        em.description='<:devv:791477096760213534>Developer <@380482923423465472>'
    em.add_field(name="<:ski:805071756633047050>Servers", value=len(client.guilds))
    em.add_field(name='<:4406_text_emoji:792921623732813856>Channels', value=f"{sum(1 for g in client.guilds for _ in g.channels)}")
    em.add_field(name="<:pythonn:791478943105941504>Library", value=f"discord.py")
    em.add_field(name="<a:pings:805073454323335218>Bot Latency", value=f"{client.ws.latency * 1000:.0f} ms")
    em.add_field(name="<:discordf:791484257688223794>vote this bot", value=f"[Click here Vote Bot](https://primebots.it/bots/788532430642348062) {client.user.name}")
    em.add_field(name="<a:starsan:805075693578747914>prefix", value=f"k/")
    em.add_field(name="<:rulesss:791488480323698719>Version Kirlia", value=f"3.1.2")
    em.add_field(name="<:staffdiscord:805116562553700354>Discord Support", value=f"[Click here  discord](https://discord.gg/s26ss5DUFf) {client.user.name}")
    em.set_footer(text="Kirlia | Powered by Kirlia Support")
    await ctx.send(embed=em)



@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"<:safy:792867515411595285>**Security Guard** `User Unbanned` {user.mention}")



@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to unban",
        )
        await ctx.send(embed=embed)
            

@client.command(description="kicks a user with specific reason (only admins)")
@commands.has_permissions(administrator=True)
async def kick (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot kick yourself!""") 

    message = f"<:safy:792867515411595285>**Security Guard** You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"{member} <:safy:792867515411595285>**Security Guard** is kicked!")
 except:
    await ctx.send(f"Error kicking user {member} (cannot kick owner or bot)")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to kick",
        )
        await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    message = f"<:safy:792867515411595285>**Security Guard** You have been Banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"<:safy:792867515411595285>**Security `Guard** user banned` {member}")
    
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to ban",
        )
        await ctx.send(embed=embed)

@client.command()
async def poll(ctx, q1, q2, time : int):
    await ctx.send(f"React with 1 to vote for **{q1}** and with 2 to vote for **{q2}**\n**Poll Lasts for {time} seconds**")

    poll = discord.Embed(title = "Poll", color = discord.Color.blue())
    poll.add_field(name = f"{q1} 1️⃣", value = "᲼᲼᲼᲼᲼᲼")
    poll.add_field(name = f"{q2} 2️⃣", value = "᲼᲼᲼᲼᲼᲼")

    msg = await ctx.send(embed = poll)

    r1 = await msg.add_reaction("1️⃣")
    r2 = await msg.add_reaction("2️⃣")

    await asyncio.sleep(time)

    await ctx.send("Times up! **Poll Closed**")

    new_msg = discord.utils.get(client.cached_messages,id = msg.id)

    users1 = await r1.reactions[0].users().flatten()
    users1.pop(users1.index(client.user))

    users2 = await r2.reactions[0].users().flatten()
    users2.pop(users2.index(client.user))

    em=discord.Embed(title=f'Votes for {q1}', description=" , ".join(user.name for user in users1),color = discord.Colour.blue())
    await ctx.send(embed = em)

    em=discord.Embed(title=f'Votes for {q2}', description=" , ".join(user.name for user in users2),color = discord.Colour.blue())
    await ctx.send(embed = em)


@poll.error
async def  poll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)




@client.command()
async def suggest(ctx, *, args):
    await ctx.message.add_reaction("🗑️")
    channel1 = client.get_channel(797102626201927680)
    embed = discord.Embed(title = "<:foglionero:805080451424583710>Suggestion from: " + ctx.author.name, color = 0x3498db)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = "<:personebelle:805080644223893504>Author's Suggestion:", value = args)
    msg = await channel1.send(embed = embed)
    await msg.add_reaction("⬆")
    await msg.add_reaction("⬇") 

@suggest.error
async def  suggest_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name=" please mention someone to execute the command or make sure you have written the command well",
        )
        await ctx.send(embed=embed)

@client.event
async def on_command_completion(ctx):
    channel = client.get_channel(797102627988307978)
    embed=discord.Embed(colour = discord.Color.blue(), title = "Command Executed")
    embed.add_field(name = "User:", value = f"`{ctx.author}`", inline = False)
    embed.add_field(name = "Channel:", value = f"{ctx.channel} **( <#{ctx.channel.id}> )**")
    embed.add_field(name = "server:", value = f"`{ctx.guild}`", inline = False)
    embed.add_field(name = "bot prefix:", value = f"`{ctx.prefix}`", inline = False)
    await channel.send(embed=embed)








@client.event
async def on_guild_join(g):
    success = False
    i = 0
    while not success:
        try:
            await g.channels[i].send(f"`Hi! Thanks for inviting me to your server k/ to` **show command list**")
        except (discord.Forbidden, AttributeError):
            i += 1
        except IndexError:
            # if the server has no channels, doesn't let the bot talk, or all vc/categories
            pass
        else:
            success = True

   
    
    payload = {
        'server_count': len(client.guilds)
    }
    

 
@client.event
async def on_guild_channel_create(channel):
  if config["configuration"]["channelsecurity"] == "enabled":
    logs = await channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create).flatten()

    user_id = logs[0].user

    final_id = client.get_user(user_id)

    await final_id.ban(reason="You are not allowed to create channels!")
  else:
    pass

@client.event
async def on_member_join(user):
  if config["configuration"]["kickbot"] == "enabled":
    if user.bot:
      await user.kick(reason="You are a bot")
    else:
      pass
  else:
    pass

@client.event
async def on_member_ban(member):
    if config["configuration"]["antiban"] == "enabled":
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        if logs.member_id != client.id:
          pass


@client.event
async def silenciarUsuario(user, razon=".", temp=120):
    await user.add_roles(discord.utils.get(user.guild.roles, name="SILENCED")) 
    embedVar = discord.Embed(title=f"YOU ARE SILENCED", color=discord.Colour.red())
    embedVar.add_field(name=f"Reason: ", value=f"{razon}!", inline=True)
    embedVar.add_field(name=f"Silence duration: ", value=f"{temp} segundos!", inline=True)
    embedVar.set_footer(text="Do not do it again or you will be sanctioned again!")
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/761574801063411712/b6560d97f36345f486cf34eb51c150d3.png?size=128")
   
    await user.send(embed=embedVar)
    await asyncio.sleep(temp)
    await user.remove_roles(discord.utils.get(user.guild.roles, name="SILENCED"))

cooldown = commands.CooldownMapping.from_cooldown(30, 30, commands.BucketType.member)
@client.event
async def on_message(msg):
    if msg.author.bot: 
        return
    if "SILENCED" in str(msg.author.roles): 
        await msg.delete()
        return
    retry_after = cooldown.update_rate_limit(msg)
    if retry_after: 
        def check(msgb):
            return msgb.author.id == msg.author.id
        await msg.channel.purge(limit=10, check=check, before=None)
        await silenciarUsuario(msg.author, razon="Send many messages")
        return
    await client.process_commands(msg) 
   




@client.command()
@commands.has_permissions(kick_members=True)
async def tempmute(ctx, member: discord.Member, time=0, reason=None):
    if reason == None:
        reason = "no reason provided"
    
    if member.id == ctx.author.id:
        await ctx.send(f"{ctx.author.mention}, you can't mute yourself")

    role = discord.utils.get(ctx.guild.roles, name="Muted")

    if role in ctx.guild.roles:
        await member.add_roles(role)
        await ctx.send(f"<:safy:792867515411595285>**Security Guard** User TempMuted {member.mention}")
        message = f"<:safy:792867515411595285>**Security Guard** You have been TempMuted from {ctx.guild.name} for {reason}"
        await member.send(message)
        await asyncio.sleep(time)
        await member.remove_roles(role)
    else:
        await ctx.send("No role named `Muted`!")



@tempmute.error
async def tempmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="you don't have permission to tempmute",
        )
        await ctx.send(embed=embed)





keep_alive.keep_alive()
secret_token = os.getenv("TOKEN")
client.run(secret_token)
