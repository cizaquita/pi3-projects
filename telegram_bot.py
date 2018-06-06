#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.

# This program is dedicated to the public domain under the CC0 license.
"""
# GPIO setup
import RPi.GPIO as GPIO
import time

# LOG Setup
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# outs and inputs SETUP
ultimaOpcion = '-1'
primerLed = 27
segundoLed = 17
tercerLed = 22
cuartoLed = 23
quintoLed = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(primerLed, GPIO.OUT)
GPIO.setup(segundoLed, GPIO.OUT)
GPIO.setup(tercerLed, GPIO.OUT)
GPIO.setup(cuartoLed, GPIO.OUT)
GPIO.setup(quintoLed, GPIO.OUT)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    print "Senial recibida..."
##    update.message.reply_text("start test")
    keyboard = [[InlineKeyboardButton("Apagar (LED1)", callback_data='0')],

                [InlineKeyboardButton("Encender (LED1)", callback_data='1')],
                
                [InlineKeyboardButton("Secuencia (LED-TODOS)", callback_data='5')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleccione una opción:', reply_markup=reply_markup)


def button(bot, update):
    global ultimaOpcion
    print "test"
    query = update.callback_query
    #update.message.reply_text("query.data = " + query.data)
    
    
    if (query.data == '0'):
        if (query.data != ultimaOpcion):
##            update.message.reply_text("LED1 encendido!")
            bot.edit_message_text(text="LED1 apagado! ",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
            GPIO.output(primerLed, False)
            ultimaOpcion = '0'
        else:
            bot.edit_message_text(text="Error: LED ya se encuentra apagado! ",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
##            update.message.reply_text("Error: LED1 ya se encuentra encendido.")
    
    if (query.data == '1'):
        if (query.data != ultimaOpcion):
##            update.message.reply_text("LED1 apagado!")
            bot.edit_message_text(text="LED1 encendido! ",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
            GPIO.output(primerLed, True)
            ultimaOpcion = '1'
        else:
            bot.edit_message_text(text="Error: LED ya se encuentra encendido! ",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
##            update.message.reply_text("Error: LED1 ya se encuentra apagado.")
    
    if (query.data == '5'):
        if (query.data != ultimaOpcion):
##            update.message.reply_text("Secuencia iniciada!")
            bot.edit_message_text(text="Secuencia iniciada! ",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
            secuencia3()
##        else:
##            update.message.reply_text("Error: LED1 ya se encuentra apagado.")



def help(bot, update):
    update.message.reply_text("Usa /start")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    try:        
        print "bot iniciado la conche tumare..."
        # Create the Updater and pass it your bot's token.
        updater = Updater("138467244:AAE-ug93RUAE5auZJNQd9TcUay0jGKhehTI")

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        updater.dispatcher.add_handler(CommandHandler('help', help))
        updater.dispatcher.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT
        updater.idle()
    
    finally:
        GPIO.cleanup()


def secuencia3():
    global ultimaOpcion
    print "Secuencia 3 iniciada..."
    ultimaOpcion = '5'
    i = 0
    while i < 70:
        print i
        GPIO.output(segundoLed, True)
	GPIO.output(tercerLed, True)
        GPIO.output(cuartoLed, True)
        GPIO.output(quintoLed, True)
        GPIO.output(primerLed, True)
	time.sleep(0.1)

        GPIO.output(segundoLed, False)
        GPIO.output(tercerLed, False)
        GPIO.output(cuartoLed, False)
        GPIO.output(quintoLed, False)
        GPIO.output(primerLed, False)
	time.sleep(0.1)
        i = i + 1
    print "Fin secuencia 3"
    ultimaOpcion = '-1'
    

if __name__ == '__main__':
    main()