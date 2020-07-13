import requests

def get_weather(lat, lon):
    return requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=1884e6b6d5605fee686cf449ac8b1e54').json()

print(get_weather(96.95, 21.83))
