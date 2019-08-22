import json

import telebot

bot = telebot.TeleBot('960428583:AAHJmP5d-xLfUINr_laOy-fPpZhFBDmwLlo')


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.reply_to(message, 'Hello, %s' % message.chat.username)


@bot.message_handler(commands=['jobs'])
def show_jobs(message):
    with open('jobs.json') as file:
        response = ''
        jobs = json.load(file)
        for i, job in enumerate(jobs):
            job['description'] = job['description']
            # response += '%d. %s - %s\n\n%s\n\n\n' % (i + 1, job['title'], job['price'], job['description'])
            response = f"{i+1}. {job['title']} - {job['price']}\n\n{job['description']}\n{job['link']}\n\n"
            bot.send_message(message.chat.id, response)


print('working')
bot.polling()



