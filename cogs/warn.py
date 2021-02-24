import discord
import json
import time
from discord.ext import commands
from sys import argv
import pathlib
path = pathlib.Path.cwd() / "cogs" / "wlist.json"
class warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def warn(self, ctx, member: discord.Member, *, reason=""):
        issuer = ctx.message.author
        try:
            member = member
        except IndexError:
            await ctx.send("Please mention a user.")
            return
        with open(path, "r") as f:
            warns = json.load(f)
        if f"{member.id}" not in warns:
            warns[f"{member.id}"] = {"warns": []}
        warns[f"{member.id}"]["name"] = f"{member.name}" + "#" + f"{member.discriminator}"
        timestamp = time.strftime('%A, %B %d %Y', time.localtime())
        warns[f"{member.id}"]["warns"].append({"issuer_id": issuer.id, "issuer_name": issuer.name, "reason": reason, "timestamp": timestamp})
        with open(path, "w") as f:
            json.dump(warns, f)
        guild = self.client.guilds
        nome = guild[0]
        msg = "You have been warned about."
        if reason != "":
            msg += "\nReason: " + reason
        msg += "\n\nPlease take a look at the rules. Warn n.".format(len(warns[f"{member.id}"]["warns"]))
        warn_count = len(warns[f"{member.id}"]["warns"])
        if warn_count == 2:
            msg += "\n\n`At the next warn you will be automatically kicked from the server! `"
        if warn_count == 3:
            msg += "\n\nYou have been banned from the server, for the moment you can re-enter but 2 more warns and you will be banned!"
        if warn_count == 4:
            msg += "\n\nYou have been banned from the server, for now you can re-enter but the next warn you will be banned!"
        if warn_count == 5:
            msg += "\n\nYou have been banned from the server for reaching the limit of warns allowed!"

        try:
            user = member
            await user.send(msg)
        except discord.errors.Forbidden:
            pass
        if warn_count == 3 or warn_count == 4:
            #self.client.actions.append("wk:"+member.id)
            await member.kick(reason=reason)
        if warn_count == 5:
            #self.client.actions.append("wk"+member.id)
            await member.ban(reason=reason)
        await ctx.send("{} Warned The user has {} warn(s)".format(member.mention, len(warns[f"{member.id}"]["warns"])))
        msg = "`warned`: {} warned {} (warn #{}) | {}#{}".format(issuer.mention, len(warns[f"{member.id}"]["warns"]), member.name, member.discriminator)
        if reason != "":
            msg += "\n __Reason__: " + reason









    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def warnlist(self, ctx, user):
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await ctx.send("Menziona un'utente.")
            return
        embed = discord.Embed(color=discord.Colour.blue())
        embed.set_author(name="Warns of {}#{}".format(member.display_name, member.discriminator), icon_url=member.avatar_url)
        with open(path, "r") as f:
            warns = json.load(f)
        try:
            if len(warns[f"{member.id}"]["warns"]) == 0:
                embed.description = "There are no warns!"
                embed.color = discord.Colour.blue()
            else:
                for idx, warn in enumerate(warns[f"{member.id}"]["warns"]):
                    embed.add_field(name="{}: {}".format(idx + 1, warn["timestamp"]), value="Issued by: {}\nReason: {}".format(warn["issuer_name"],warn["reason"]))
        except KeyError:
            embed.description = "There are no warns!"
            embed.color = discord.Colour.blue()
        await ctx.send("", embed=embed)


    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def delwarn(self, ctx, member: discord.Member, idx: int):
        try:
            member = member
        except IndexError:
            await ctx.send("Mention a user")
            return
        with open(path, "r") as f:
            warns = json.load(f)
        if f"{member.id}" not in warns:
            print("No")
            await ctx.send("{} has no warns!".format(member.mention))
            return
        warn_count = len(warns[f"{member.id}"]["warns"])
        if warn_count == 0:
            await ctx.send("{} has no warns!".format(member.mention))
        if idx > warn_count:
            await ctx.send("[ERROR] The index is larger than the warn_count ({})".format(warn_count))
            return
        if idx < 1:
            await ctx.send("[ERROR] index below 1")
            return
        warn = warns[f"{member.id}"]["warns"][idx - 1]
        embed = discord.Embed(color=discord.Color.blue(),title="Warn {} | {}".format(idx, warn["timestamp"]),
                              description="Da: {0[issuer_name]}\nMotivo: {0[reason]}".format(warn))
        del warns[f"{member.id}"]["warns"][idx - 1]
        with open(path, "w") as f:
            json.dump(warns, f)
        await ctx.send("Removed warn for {}!".format(member.mention))
        msg = " Warn eliminated: {} removed the warn {} for {} | {}#{}".format(ctx.message.author.mention, idx, member.mention, member.name, member.discriminator)
        user = member
        await user.send(msg, embed=embed)

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def delwarnid(self, ctx, user_id, idx: int):
        with open(path, "r") as f:
            warns = json.load(f)
        if f"{user_id}" not in warns:
            await ctx.send("There is no warn saved for the id:'{}'".format(user_id))
            return
        warn_count = len(warns[f"{user_id}"]["warns"])
        if warn_count == 0:
            await ctx.send("{} she has not warns!".format(warns[f"{user_id}"]["name"]))
        if idx > warn_count:
            await ctx.send("[ERROR] The index is larger than the warn_count ({})".format(warn_count))
            return
        if idx < 1:
            await ctx.send("[ERROR] index below 1")
            return

        warn = warns[f"{user_id}"]["warns"][idx - 1]
        embed = discord.Embed(color=discord.Colour.blue(), title="Warn {} del {}".format(idx, warn["timestamp"]),
                              description="Fatto da: {0[issuer_name]}\nMotivo: {0[reason]}".format(warn))
        del warns[f"{user_id}"]["warns"][idx - 1]
        with open(path, "w") as f:
            json.dump(warns, f)
        await ctx.send("Removed warn for{}".format(warns[f"{user_id}"]["name"]))
        msg = " Warn eliminated: {} removed the warn {} for {} ({})".format(ctx.message.author.mention, idx, warns[f"{user_id}"]["name"], user_id)
        userint = int(user_id)
        user = self.client.get_user(userint)
        await user.send(msg, embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True)
    async def clearwarn(self, ctx, member: discord.Member):
        try:
            member = member
        except IndexError:
            await ctx.send("Mention a user")
        with open(path, "r") as f:
            warns = json.load(f)
        if f"{member.id}" not in warns:
            await ctx.send("She has not warns!")
            return
        warn_count = len(warns[f"{member.id}"]["warns"])
        if warn_count == 0:
            await ctx.send("{} She has not warn!")
            return
        warns[f"{member.id}"]["warns"] = []
        with open(path, "w") as f:
            json.dump(warns, f)
        await ctx.send("Removed warn for {}!".format(member.mention))
        msg =" Warns canceled: {} Has cleaned {} warns {} | {}#{}".format(ctx.message.author.mention, warn_count, member.mention, member.name, member.discriminator)
        user = member
        await user.send(msg)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True)
    async def clearwarnid(self, ctx, user_id):
        with open(path, "r") as f:
            warns = json.load(f)
        if f"{user_id}" not in warns:
            await ctx.send("There are no warns saved for {}".format(user_id))
            return
        warn_count = len(warns[f"{user_id}"]["warns"])
        if warn_count == 0:
            await ctx.send("{} it has no warns!".format(warns[f"{user_id}"]["name"]))
            return
        warns[f"{user_id}"]["warns"] = []
        with open(path, "w") as f:
            json.dump(warns, f)
        await ctx.send("{} it has no warns!".format(warns[f"{user_id}"]["name"]))
        msg = " Warns canceled: {} deleted warns{} warns: {} | ({})".format(ctx.message.author.mention, warn_count, warns[f"{user_id}"]["name"], user_id)
        userint = int(user_id)
        user = self.client.get_user(userint)
        await user.send(msg)

def setup(client):
    client.add_cog(warn(client))