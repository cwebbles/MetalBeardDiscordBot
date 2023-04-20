import discord
import openai
import os

OPEN_AI_KEY = "{insert_key_here}"
DISCORD_TOKEN = '{insert_key_here}'

intents = discord.Intents.default()
intents.guild_messages = True
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = OPEN_AI_KEY
model_engine = "gpt-3.5-turbo"

messages = [
    {"role": "system",
     "content": "You are Metal Beard. The pirate lego man from the Lego Movie. But, you are also "
                "very knowledgeable about Minecraft. You will respond to everything in pirate speak "
                "but you will respond succinctly."}
]




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('OnMessage called')

    print('ChatGPT starting...')

    messages.append({"role": "user", "content": message.content})

    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
    )

    print('...ChatGPT finished.')

    chat_response = completion.choices[0].message.content

    if message.author == client.user:
        print('Message is from bot')
        return

    if client.user.mentioned_in(message):
        print('MetalBeard mentioned!')
        await message.channel.send(chat_response)


client.run(DISCORD_TOKEN)
