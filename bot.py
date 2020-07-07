# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(token_for_bot)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'HI')


bot.polling()
