import discord
from discord.ext import commands
from variables import *
from discord.commands import slash_command
import random

import aiosqlite

class LevelSytem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        async with aiosqlite.connect("level.db") as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                msg_count INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0
                )
                """
            )

    @commands.Cog.listener()
    async def on_message(self, message):
        async with aiosqlite.connect("level.db") as db:
            await db.execute(
                    "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.author.id,)
            )
            await db.execute(
                    "UPDATE users SET msg_count = msg_count + 1 WHERE user_id = ?", (message.author.id,)
            )
            await db.execute(
                    "UPDATE users SET xp = xp + ? WHERE user_id = ?", (random.randint(20,40), message.author.id)
            )
            await db.commit()

    @slash_command()
    async def rank(self, ctx):
        async with aiosqlite.connect("level.db") as db:
            async with db.execute("SELECT msg_count, xp FROM users WHERE user_id = ?", (ctx.author.id,)) as cursor:
                result = await cursor.fetchone()
                if result is None:
                    await ctx.respond("You haven't chatted yet", ephemeral=True)
                    return
                msg_count, xp = result

        await ctx.respond(f"You've sent **{msg_count}** messages and got **{xp}** xp!")
                    

def setup(bot):
    bot.add_cog(LevelSytem(bot))
