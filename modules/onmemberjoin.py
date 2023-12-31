import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from variables import *
import random

class onmemberjoin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.chan = 0

    #initializes the channel for the welcome message :P
    @discord.default_permissions(manage_channels=True)
    @slash_command()
    async def initchannel(self, ctx, channel: Option(discord.TextChannel)):
        await ctx.respond(f"{channel} is now the welcome channel :>",ephemeral=True)
        self.chan = channel.id

    #if a member joins this will be executed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title=f"Welcome!",
            description=f"I hope you'll have a nice and comfy arrival {member.mention}! :>",
            color=0xFFFFFF
        )
        channel = await self.bot.fetch_channel(self.chan)        
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(onmemberjoin(bot))