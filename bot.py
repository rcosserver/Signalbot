# -*- coding: utf-8 -*-

import config
import datetime
import telebot
import pyowm

tempID = config.appid
bot = telebot.TeleBot(config.token)


#Месяц
today = datetime.datetime.today()
mount = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
mounth_real = int(today.strftime("%m"))



#Погода в Москве
temp = pyowm.OWM(tempID, {'language': 'ru'})
observation = owm.weather_at_place('Москва')
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']


text1 = ('Привет, сегодня ' + today.strftime("%d") + ' ' + mount[mounth_real % 12] + ' ' + today.strftime("%Y") + ' г.')
text2 = ('Погода в Москве хорошая, ' + w.get_detailed_status()+ ' ' + str(temp) + ' °C')


@bot.message_handler(content_types=["text"])
def message(message):
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)



bot.polling(none_stop=True, interval=0)

















