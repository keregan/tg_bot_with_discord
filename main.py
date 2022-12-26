import requests
import time
import json
import telebot
import asyncio
import discord
import requests
import apy_bot
import random
import threading

from discord.ext import commands
from aiogram import Bot, Dispatcher, executor, types
from concurrent.futures import ThreadPoolExecutor

last_message = ({"last_mess"})

# headers = {"user agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro"
#                          "me/102.0.0.0 Safari/537.36"}
# url = "https://yobit.net/api/3/info"


bot_telegramm = Bot(token=apy_bot.telebot_api)
dp_telegramm = Dispatcher(bot_telegramm)

bot_discord = commands.Bot(intents=discord.Intents.default(), command_prefix='><')
client_discord = discord.Client(intents=discord.Intents.default())


def telegramm_send_all(text):
    params = {
        'chat_id': apy_bot.user_id,
        'text': text,
    }
    response = requests.get('https://api.telegram.org/bot' + apy_bot.telebot_api + '/sendMessage', params=params)


@bot_discord.event
async def on_ready():
    while True:
        # await tester()
        # print("Discord_bot on_ready")
        await last_message()
        random_poss = random.randint(55, 180)
        random_poss = 3
        await asyncio.sleep(random_poss)


@bot_discord.event
async def tester():
    channel = bot_discord.get_channel(982160360897396736)
    await channel.send("test")


@bot_discord.event
async def last_message():
    global  text_message
    channel = bot_discord.get_channel(982160360897396736)
    messages = [message async for message in channel.history(limit=1)]

    for msg in messages:
        # text_author = msg.author
        text_message = str(msg.author)[:-5] + " " + str(msg.created_at.strftime('%Y-%m-%d %H:%M:%S')) + " " + str(msg.content)
        # text_datatime = msg.created_at
        # text_jet = str(msg.author)[:-5] + " " + str(msg.created_at.strftime('%Y-%m-%d %H:%M:%S')) + " " + str(msg.content)
        # print(text_jet)

    try:
        with open('last_message.json', encoding='utf-8') as file_json:
            last_message = json.load(file_json)

        if text_message != last_message["last_mess"]:
            telegramm_send_all(text_message)
            print(text_message)
            last_message["last_mess"] = text_message
            with open("last_message.json", "w", encoding='utf-8') as file_json:
                json.dump(last_message, file_json, indent=4, ensure_ascii=False)
    except:
        pass


@dp_telegramm.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp_telegramm.message_handler()
async def echo(message: types.Message):
    text = message.text
    await message.answer(text)


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(bot_discord.start(apy_bot.discord_api))
    print("Discord_bot activated")
    print("Telegramm_bot activated")
    executor.start_polling(dp_telegramm)
    loop.run_forever()


if __name__ == '__main__':
    main()
