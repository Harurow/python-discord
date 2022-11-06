#!/usr/local/bin/python3

import os
import discord
from dotenv import load_dotenv
load_dotenv(override=True)

# 認証情報は.envから取得する
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    for channel in client.get_all_channels():
        if channel.type == discord.ChannelType.text:
            if (channel.name == 'api-test'):
                await channel.send('Hello!')

    await client.close()

client.run(TOKEN)
