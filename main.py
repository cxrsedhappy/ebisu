import asyncio
import os
import discord
from discord.ext import commands

APP_ID = 1
SERVER_ID = 1
TOKEN = ''
GUILD = discord.Object(SERVER_ID)

intents = discord.Intents.all()


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents, application_id=APP_ID)

    async def on_ready(self):
        for fn in os.listdir("./cogs"):
            if fn.endswith(".py"):
                await client.load_extension(f'cogs.{fn[:-3]}')

        await self.tree.sync(guild=GUILD)
        print('Connected and synced')


async def main():
    await client.start(TOKEN)


client = Client()
asyncio.run(main())