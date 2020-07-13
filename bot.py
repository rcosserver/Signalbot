import datetime
import requests
import json

appid = "1884e6b6d5605fee686cf449ac8b1e54"

today = datetime.datetime.today()
mount = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']

mounth_real = int(today.strftime("%m"))

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'id': 524901, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print('Привет, сегодня', today.strftime("%d"),mount[mounth_real % 12],today.strftime("%Y"),'г.')

#---------------------#

print('Погода в Москве хорошая,', data['weather'][0]['description'],',',data['main']['temp'], 'градуса Цельсия')






