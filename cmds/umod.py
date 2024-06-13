from discord.ext import commands

@commands.group()
async def umod(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'{ctx.subcommand_passed} does not belong to User mod commands!')

@umod.command()
async def kick(ctx):
    pass

@umod.command()
async def ban(ctx):
    pass

@umod.command()
async def mute(ctx):
    pass

async def setup(bot):
    bot.add_command(umod)