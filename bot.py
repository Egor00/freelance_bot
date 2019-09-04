import json

import telebot

from settings import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.reply_to(message, "Hello, %s! \n Send '/jobs' to get offers" % message.chat.username)


@bot.message_handler(commands=['jobs'])
def show_jobs(message):
    with open('jobs.json') as file:
        jobs = json.load(file)
        for i, job in enumerate(jobs):
            job['description'] = job['description']
            response = f"{i+1}. {job['title']} - {job['price']}\n\n{job['description']}\n{job['link']}\n\n"
            bot.send_message(message.chat.id, response)

bot.polling()



