import discord

from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice, Command

from callbacks import command_callbacks


SERVER_ID = 974988972864471061
GUILD = discord.Object(SERVER_ID)

intents = discord.Intents.all()


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        print(f"Loaded {self.__cog_name__}")

    @app_commands.command(name='create', description='creates new application command')
    @app_commands.guilds(GUILD)
    @app_commands.choices(_type=[
        Choice(name='default', value=1),
        Choice(name='special', value=2),
        Choice(name='param', value=3),
    ])
    async def create_command(self, interaction: discord.Interaction, name: str, description: str, _type: Choice[int]):
        match _type.value:
            case 1:
                command = Command(name=name,
                                  description=description,
                                  callback=command_callbacks.DEFAULT_CALLBACK,
                                  guild_ids=[SERVER_ID])
            case 2:
                command = Command(name=name,
                                  description=description,
                                  callback=command_callbacks.SPECIAL_CALLBACK,
                                  guild_ids=[SERVER_ID])
            case 3:
                command = Command(name=name,
                                  description=description,
                                  callback=command_callbacks.PARAM_CALLBACK,
                                  guild_ids=[SERVER_ID])

        self.bot.tree.add_command(command)
        await interaction.response.send_message('Done', ephemeral=True)

    @app_commands.command(name='sync', description='sync new commands to your guild')
    @app_commands.guilds(GUILD)
    async def sync_command(self, interaction: discord.Interaction):
        # WARNING! Do not sync your every command if you want to add >1 app_commands
        # It is bad practice
        await self.bot.tree.sync(guild=GUILD)
        await interaction.response.send_message('Synced', ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(TestCog(bot))
