import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def about(ctx):
    await ctx.send("This bot is created to demonstrate commands on Discord.")

@bot.command()
async def commands(ctx):
    await ctx.send("Available commands: about, commands, command, author, open_source, github, gitlab, website, site, telegram")

@bot.command()
async def command(ctx, cmd: str):
    await ctx.send(f"Description of {cmd} command: ...")

@bot.command()
async def author(ctx):
    await ctx.send("Author of this bot: your_name")

@bot.command()
async def open_source(ctx):
    await ctx.send("Source code of this bot is available at: https://github.com/your_username/your_bot")

@bot.command()
async def github(ctx):
    await ctx.send("GitHub repository: https://github.com/your_username/your_bot")

@bot.command()
async def gitlab(ctx):
    await ctx.send("GitLab repository: https://gitlab.com/your_username/your_bot")

@bot.command()
async def website(ctx):
    await ctx.send("Bot's website: https://yourbotwebsite.com")

@bot.command()
async def site(ctx):
    await ctx.send("Bot's website: https://yourbotwebsite.com")

@bot.command()
async def telegram(ctx):
    await ctx.send("Telegram bot: @your_telegram_bot")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run('#')
