# import requests
# import time
# import json
# import telebot
# import config
import apy_bot

from aiogram import Bot, Dispatcher, executor, types

# headers = {"user agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro"
#                          "me/102.0.0.0 Safari/537.36"}
# url = "https://yobit.net/api/3/info"

bot = Bot(token=apy_bot.telebot_api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)


