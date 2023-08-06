import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from variables import *
import random

class slashes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # / command that randomly sends cakes :3
    @slash_command(name='cake', description="cake!!!")
    async def cake(self, ctx):
        response = random.choice(kuchenn)
        await ctx.send(response)
        await ctx.respond("cake send :3", ephemeral=True)

    @slash_command(name='soup', description="gives you a nice little soup!")
    async def soup(self, ctx):
        response = random.choice(soup)
        await ctx.send(respond)
        await ctx.respond("soup send :3", ephemeral=True)

    # / command that randomly sends a cat meme :>
    @slash_command(name='glalacat', description="cet!!!")
    async def glalacet(self, ctx):
        response = random.choice(cat)
        await ctx.send(response)
        await ctx.respond("cet send :3", ephemeral=True)

def setup(bot):
    bot.add_cog(slashes(bot))
