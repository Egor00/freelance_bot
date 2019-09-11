import json
import time

import telebot

from db_models import User, Parameter
from settings import BOT_TOKEN
from spider_runner import crawl

from db import session

bot = telebot.TeleBot(BOT_TOKEN)


def update_data_loop():
    while True:
        # crawl('python')
        time.sleep(60 * 60)


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    user_id = message.from_user.id
    user = session.query(User).get(user_id)
    if user is None:
        user = User(id=user_id)
        session.add(user)
        session.commit()
    bot.reply_to(message, "Hello, %s! \n Send '/jobs' to get offers" % message.chat.username)


@bot.message_handler(commands=['jobs'])
def show_jobs(message):
    with open('jobs.json') as file:
        jobs = json.load(file)
        for i, job in enumerate(jobs):
            job['description'] = job['description']
            response = f"{i + 1}. {job['title']} - {job['price']}\n\n{job['description']}\n{job['link']}\n\n"
            bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['addPar'])
def add_parameter(message):
    user = session.query(User).get(message.chat.id)
    if user is None:
        bot.send_message(message.chat.id, 'Send /start previously')
        return
    parameters_str = message.text.replace(',', ' ').split()[1:]
    parameters = {Parameter(par=par_str) for par_str in parameters_str}
    exi_pars = session.query(Parameter).all()
    filter(lambda x: x.par in parameters_str, exi_pars)
    parameters -= set(session.query(Parameter))
    parameters.update(exi_pars)
    user.sub_pars.update(parameters)
    session.commit()
    parameters_str = {repr(par_str) for par_str in parameters_str}
    response = 'Parameters added: ' + ', '.join(parameters_str)
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['delPar'])
def del_parameter(message):
    user = session.query(User).get(message.chat.id)
    parameters_str = message.text.replace(',', ' ').split()[1:]
    parameters = session.query(Parameter).all()
    filter(lambda x: x.par in parameters_str, parameters)
    user.sub_pars.remove(parameters)
    response = 'Parameters deleted: ' + ', '.join(parameters_str)
    bot.send_message(message.chat.id, response)






'''@bot.message_handler(commands=['dropPar'])
def drop_par(message):
    pars = session.query(Parameter)
    for par in pars:
        session.delete(par)
    session.commit()
    bot.send_message(message.chat.id, 'done')'''
