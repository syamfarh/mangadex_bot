import os
import telebot
import time
from prawReddit import prawReddit
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Will pull links from Reddit!")

    while True:
        for link in prawReddit():
            bot.send_message(message.chat.id, link)
        bot.send_message(message.chat.id, "going to sleep!")
        time.sleep(1800)

bot.polling(none_stop=True)
