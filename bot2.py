#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import requests
from io import BytesIO

url = "https://proyecto-uem-2021-predict-comedic-puku-ex.eu-gb.mybluemix.net/predict"


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("Lo siento, mi creador solo me dio creo con una neurona y solo puedo predecir numeros.")
    update.message.reply_text("Enviame una foto y tratare de adivinal el numero escrito.")

def picture(update, context):
    """Echo the user message."""
    #r = requests.post(url, files=update.message.photo)
    my_img = {'image': open('test.png', 'rb')}
    r = requests.post(url, files=my_img) 
    print("Eso parece un ",r.json()['Predicted value'])
    update.message.reply_text("Eso parece una F")
    #update.message.reply_text("bonita foto")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def picture2(update, context):
    file = context.bot.get_file(update.message.photo[-1].file_id)
    picture =  BytesIO(file.download_as_bytearray())
    #r = requests.post(url, files=picture) 
    #print("Eso parece un ",r.json()['Predicted value'])
    update.message.reply_text("bonita foto")
    


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1891152755:AAEMFvvqgMaL7x9QWZ7psj5sHhpjNbFAl-Y", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    # picture answer beautifull picture
    dp.add_handler(MessageHandler(Filters.photo, picture2))   

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()