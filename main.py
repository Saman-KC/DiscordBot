import discord ,os, random , pathlib
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands


#env variables
load_dotenv()
TOKEN= os.getenv('TOKEN')

#commands path listing
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        ranuser = random.choice(ctx.guild.members)
        return (f'{ctx.author.mention} slapped {ranuser.mention} {argument}')

#run the bot
def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.reactions = True
    intents.members = True
    bot = commands.Bot(command_prefix=".", intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is running!!!')
        await bot.tree.sync()

        for cmd_file in CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")


    @bot.event
    async def on_command_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument!')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found ! Try checking your spelling!')


    @bot.hybrid_command(name="ping", description="none")
    async def ping(ctx):
        await ctx.send('pong',ephemeral=True)
    
    @bot.hybrid_command(name="say", description="none")
    async def say(ctx, value: app_commands.Range[str, None, 1000]):
        await ctx.send(value)

    @bot.command()
    async def slap(ctx, * , reason : Slapper):
        await ctx.send(reason)

    bot.run(TOKEN)

if __name__ == '__main__':
    run_bot()