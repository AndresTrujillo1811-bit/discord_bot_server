import discord
import random

import config
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)
token = config.DISCORD_TOKEN

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(config.WELCOME_CHANNEL_ID)

    if channel is None:
        print("Channel not found")
        return

    await channel.send(
        f"Hello {member.mention}!"
        f"Welcome to {member.guild.name}"
    )

@bot.event
async def on_message(message):
    username = message.author.display_name
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f"Message {user_message} by {username} on {channel}")

    if message.author == bot.user:
        return

    if channel == "general":
        if user_message.lower() in ("heeey", "hi", "hello", "what's up, wassup", "hey"):
            await message.channel.send(f"Hello {username}!")
            return

        elif user_message.lower() in ("bye", "see u", "see you", "goodbye"):
            await message.channel.send(f"Bye {username}!")

        elif "time" in user_message.lower() or "clock" in user_message.lower():
            current_time = datetime.now().strftime("%H:%M")
            await message.channel.send(f"The clock is {current_time}.")

        elif "year" in user_message.lower():
            current_year = datetime.now().year
            await message.channel.send(f"The year is {current_year}!")

        elif "food" in user_message.lower():
            foods = ["Sushi", "Pizza", "Hamburger", "Pasta", "Tacos"]
            await message.channel.send(f"I like {random.choice(foods)}")

        elif "drink" in user_message.lower():
            drinks = ["Coca-Cola", "Oreo milkshake", "Coffee", "Fanta", "Tea", "Beer"]
            await message.channel.send(f"I like {random.choice(drinks)}")

        elif "hobby" in user_message.lower():
            hobbies = ["watch football", "play videogames", "listen to music", "code programs", "watch series"]
            await message.channel.send(f"I like to {random.choice(hobbies)}")


bot.run(token)
