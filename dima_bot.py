import pyowm
import telebot
import datetime
import time
#import pycbrf

from pyowm import OWM
from telebot import types
#from pycbrf.toolbox import ExchangeRates

#Токены
owm = pyowm.OWM('*******', language= 'RU')
bot = telebot.TeleBot('*******')

#Погода в Москве
observation = owm.weather_at_place('Москва')
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']

#date & time
a = datetime.datetime.today().strftime("%Y%m%d")
today = datetime.datetime.today()
times = datetime.datetime.today().strftime("%H%M%S")
#print (times)

#день и месяц текстом
day = today.strftime("%A")
if day == 'Monday':
    day = 'понедельник'
elif day == 'Tuesday':
    day = "вторник"
elif day == 'Wednesday':
    day = "среда"
elif day == 'Thursday':
    day = "четверг"

mouth = today.strftime("%m")
if mouth == '07':
    mouth = "июля"

#курс валют
#rates = ExchangeRates()
#usd_name = rates['USD'].name
#usd = rates['USD'].value
#print(usd_name, usd)
#euro_name = rates['EUR'].name
#euro = rates['EUR'].value
#print(euro_name, euro)

#Телефонный справочник
database = [
    ["Парфенов", "Дмитрий", "Викторович", "89859901024", 'Отдел ОК', "455"],
    ["Парфенов", "Андрей", "Викторович", "89859923724", "Отдел АРМ", "288"],
    ["Миликов", "Максим", "Олегович", "89161438251", 'Отдел ОК', "185"],
    ["Клюев", "Дмитрий", "Алексеевич", "89857628011", 'Отдел ОК', "292"],
     ]



#print("Нет такого!")
    #if i == "Дмитрий":
     #   print(i)
hello = (f"Привет, cегодня {day} " + today.strftime("%d") + " " + mouth + " " + today.strftime("%Y") + " года в Москве сейчас " + w.get_detailed_status() + ', температура в районе ' + str(temp) + '°C. Курс валют на сегодня: ')
zapros = '';
tel_number = '';

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, hello)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "/start - начало, /tel - телефонная книга,")

@bot.message_handler(commands=['tel'])
def tel(message):
    bot.send_message(message.chat.id, "Телефонная книга, введи ФИО или номер сотрудника:");
    bot.register_next_step_handler(message, find);

@bot.message_handler(content_types=['text'])
def on(message):
    bot.send_message(message.chat.id, "Введи команду /help для начала работы");


def find(message):
    global zapros;
    global tel_number;
    zapros = message.text;
    for i in database:
        if zapros == i[0]:
            tel_number = " ".join(i);
            bot.send_message(message.chat.id, tel_number)
        elif zapros == i[1]:
            tel_number = " ".join(i);
            bot.send_message(message.chat.id, tel_number)
        elif zapros == i[3]:
            tel_number = " ".join(i);
            bot.send_message(message.chat.id, tel_number)
        elif zapros == i[5]:
            tel_number = " ".join(i);
            bot.send_message(message.chat.id, tel_number)
    if tel_number == '':
        bot.send_message(message.chat.id, "Нет такого товарища!")
    tel_number = ''





bot.polling(none_stop=True, interval=0)
