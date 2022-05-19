import discord


async def default_callback(interaction: discord.Interaction):
    await interaction.response.send_message('Hello from your command')


async def special_callback(interaction: discord.Interaction):
    embed = discord.Embed(title='Special callback')
    embed.add_field(name='Welcome here', value='My new command')
    await interaction.response.send_message(embed=embed)


async def param_callback(interaction: discord.Interaction, number: int):
    await interaction.response.send_message(f'Your number is {number}! Boo!')


DEFAULT_CALLBACK = default_callback
SPECIAL_CALLBACK = special_callback
PARAM_CALLBACK = param_callback
