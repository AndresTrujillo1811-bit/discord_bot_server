import discord
import random
import config

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

bot = discord.Client()
token = config.DISCORD_TOKEN

@bot.event
async def starting_bot():
    print(f"Logged in as {bot.user}")

@bot.event
async def welcome_message(member):
    channel = bot.get_channel(config.WELCOME_CHANNEL_ID)

    if channel is None:
        print("Channel not found")
        return

    await channel.send(
        f"Hello {member.mention}!"
        f"Welcome to {member.guild.name}"
    )

@bot.event
async def bot_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f"Message {user_message} by {username} on {channel}")

    if message.author == bot.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f"Hello {username}!")
            return

        elif user_message.lower() in ("bye", "see u", "see you", "goodbye"):
            await message.channel.send(f"Bye {username}!")

        elif user_message.lower() == "time" or user_message == "clock":
            current_time = datetime.now().strftime("%H:%M")
            await message.channel.send(f"The clock is {current_time}.")

        elif user_message.lower() == "year":
            current_year = datetime.now().year
            await message.channel.send(f"The year is {current_year}!")

        elif user_message.lower() == "food":
            foods = ["Sushi", "Pizza", "Hamburger", "Pasta", "Tacos"]
            await message.channel.send(f"I like {random.choice(foods)}")    

