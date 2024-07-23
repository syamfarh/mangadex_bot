import os
import telebot
import time
import nonPersisData as npd
from prawReddit import prawReddit, subExists
from dotenv import load_dotenv


load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    npd.add_user(message.from_user.id)
    bot.reply_to(message, "Welcome! Will pull links from Reddit!")
    subreddit_handler(message)

@bot.message_handler(commands=['subreddit'])
def subreddit_handler(message):
    npd.off_loop(message.from_user.id)
    npd.update_recent_id(message.from_user.id)
    message = bot.send_message(message.chat.id, "Choose a subreddit to pull from: ")
    bot.register_next_step_handler(message, check_subreddit)

@bot.message_handler(commands=['keyword'])
def handle_keyword(message):
    npd.off_loop(message.from_user.id)
    message = bot.send_message(message.chat.id, "Enter a keyword: ")
    bot.register_next_step_handler(message, add_keyword)

def check_subreddit(message):
    if not(subExists(message.text)):
        message = bot.send_message(message.chat.id, "That subreddit does not exist. Please try again: ")
        bot.register_next_step_handler(message, check_subreddit)
    else:
        npd.add_subreddit_to_user(message)
        handle_keyword(message)

def add_keyword(message):
    npd.add_keyword_to_user(message)
    npd.on_loop(message.from_user.id)
    scrape_subreddit(message)

def scrape_subreddit(message):
    while (npd.user_data[message.chat.id]["cont_loop"] == npd.user_data[message.chat.id]["subreddit"]):
        for link in prawReddit(npd.user_data[message.chat.id]):
            bot.send_message(message.chat.id, link)
        bot.send_message(message.chat.id, "going to sleep!")
        print(npd.user_data)
        time.sleep(10)
    return

bot.polling(none_stop=True)
