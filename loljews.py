#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Job
from scrape import scrape
import logging

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def anime(bot, update):
    if scrape() is False:
        result = "A porca não tá cá.."
    else:
        result = "A puta da animegamergirl tá online a enficar coisas no cu!"
    bot.sendMessage(chat_id=update.message.chat_id, text=result)

        #bot.sendMessage(chat_id='-31059729', text=result)

def main():
    updater = Updater(token='302715001:AAH2EV86w3VrXgWmkLZn33A8riBueu6d1a0')
    #jobs = updater.job_queue
    dispatcher = updater.dispatcher
    logging.basicConfig(level=logging.INFO)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    anime_handler = CommandHandler('anime', anime)
    dispatcher.add_handler(anime_handler)
    #job_minute = Job(auto_anime, 60.0)
    #jobs.put(job_minute, next_t=0.0)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

