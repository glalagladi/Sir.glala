import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from variables import *
import random

class administration(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # / kick command
    @slash_command(name='kick', description='this command lets you kick members (only with permissions)')
    @discord.default_permissions(kick_members=True)
    async def kick(self, ctx, member: Option(discord.Member), *, reason=None):
        try:
            await member.kick(reason=reason)
        except discord.Forbidden:
            await ctx.respond("You don't have the permissions to do that!")
        
        await ctx.respond(f"{member} got kicked from {ctx.author} because of {reason}!")
        print(f"{member} got kicked from {ctx.author} because of {reason}!")

    # / ban command
    @slash_command(name='ban', description='this command lets you kick members (only with permissions)')
    @discord.default_permissions(ban_members=True)
    async def ban(self, ctx, member: Option(discord.Member), *, reason=None):
        try:
            await member.ban(reason=reason)
        except discord.Forbidden:
            await ctx.respond("You don't have the permissions to do that!")
        
        await ctx.respond(f"{member} got banned from {ctx.author} because of {reason}!")
        print(f"{member} got banned from {ctx.author} because of {reason}!")

def setup(bot):
    bot.add_cog(administration(bot))
