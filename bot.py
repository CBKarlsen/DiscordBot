import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rps(ctx, choice: str):
    valid_choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(valid_choices)

    if choice.lower() not in valid_choices:
        await ctx.send("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    result = determine_winner(choice.lower(), bot_choice)
    await ctx.send(f"Bot chose {bot_choice}. {result}!")

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'scissors' and bot_choice == 'paper') or \
         (player_choice == 'paper' and bot_choice == 'rock'):
        return "You win"
    else:
        return "Bot wins"

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"The coin landed on {result}!")

@bot.command()
async def linda(ctx):
    await ctx.send("Linda er deilig")


bot.run('.YOUR TOKEN HERE')

"https://discord.com/developers/applications"
