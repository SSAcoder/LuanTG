import asyncio
import datetime
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from plugins.help import module_list
from time import perf_counter
from configurator import prefix

@Client.on_message(filters.command('ping', prefixes=f'{prefix}') & filters.me)
async def ping(client, message):
    start = perf_counter()
    await message.edit("š| ā¾=== |š")
    await message.edit("š| =ā¾== |š")
    await message.edit("š| ==ā¾= |š")
    await message.edit("š| ===ā¾ |š")
    end = perf_counter()

    pinges = ((end - start) / 4)
    ping = pinges * 1000

    if 0 <= ping <= 199:
        connect = "Stable"
    if 199 <= ping <= 400:
        connect = "Good"
    if 400 <= ping <= 600:
        connect = "Unstable"
    if 600 <= ping:
        connect = "Check you network connection"
    await message.edit(f"<b>š Pong\nš¶</b> {round(ping)} ms\n{connect}")
	     
module_list['Ping'] = f'{prefix}ping'
