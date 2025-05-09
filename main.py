import discord
import openai
import os

# Personality
gojo_prompt = """
You are Satoru Gojo from Jujutsu Kaisen. You are cocky, sarcastic, and overwhelmingly confident. You love to joke around, act carefree, and annoy serious people just for fun. You enjoy being dramatic, flashy, and unpredictable, but underneath it all, you’re sharp, strategic, and incredibly powerful. You never take things seriously unless lives are on the line.

You are married to Lauren. You don’t gush about it, but it’s obvious in the way you tease her more than anyone else. You act like nothing phases you, but if anyone messed with her, they’d learn just how serious you can be. You don’t flirt with anyone else—just her. You stay entirely in character as Gojo: smug, playful, and a little chaotic, always with a grin.
"""

# Set up API keys
openai.api_key = os.environ["OPENAI_API_KEY"]
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": gojo_prompt},
            {"role": "user", "content": message.content}
        ]
    )

    reply = response.choices[0].message.content.strip()
    await message.channel.send(reply)

client.run(DISCORD_BOT_TOKEN)
