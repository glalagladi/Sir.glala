from discord.ext import commands
from discord.commands import slash_command
from variables import *
import random

class onmessage(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        #await bot.process_commands(message)
        if message.author == self.bot.user:
            return

        if message.content.lower().replace(" ","") == 'glalaisafemboy':
            response = random.choice(femboy)
            await message.channel.send(response)
            print(f'succesfully loaded femboy mode result = {response}')

        if message.content.lower() == 'tubig':
            response = random.choice(tubig)
            await message.channel.send(response)
            print('succesfully loaded tubig mode')

        if message.content.lower() == 'glalameme':
            response = random.choice(glala)
            await message.channel.send(response)
            print('succesfully loaded glala mode')

        if message.content.lower() == 'bonni':
            response = random.choice(bonni)
            await message.channel.send(response)
            print('succesfully loaded bonni mode')

        if message.content.lower() == 'uwu':
            response = random.choice(UwU)
            await message.channel.send(response)
            print('succesfully loaded UwU mode')

        if message.content.lower() == 'hey':
            response = random.choice(hey)
            await message.channel.send(response)
            print('succesfully loaded hey')

        if message.content.lower().replace(" ", "") == 'ieatdirt':
            response = random.choice(ieatdirt)
            await message.channel.send(response)
            print('succesfully loaded ieatdirt')

        if message.content.lower().replace(" ", "") == 'ilovesir.glala':
            response = random.choice(love3)
            await message.channel.send(response)
            print('succesfully loaded love3')

        if message.content.lower().replace(" ", "") == 'ilovelean':
            response = random.choice(lean)
            await message.channel.send(response)
            print('succesfully loaded lean')

        if message.content.lower() == 'susuyong':
            response = random.choice(suyong)
            await message.channel.send(response)
            print('succesfully loaded suyong mode')

        if message.content.lower() == 'bruh':
            response = random.choice(bruh)
            await message.channel.send(response)
            print('succesfully loaded bruh mode')

        if message.content.lower() == 'guh':
            response = random.choice(guh)
            await message.channel.send(response)
            print('succesfully loaded guh mode')

        if message.content.lower() == "sui":
            response = random.choice(sui)
            await message.channel.send(response)
            print("succesfully loaded sui mode")


def setup(bot):
    bot.add_cog(onmessage(bot))
