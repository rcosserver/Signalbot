import requests
city_id = 524901
appid = "1884e6b6d5605fee686cf449ac8b1e54"

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': 524901, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
except Exception as e:
    print("Exception (weather):", e)
    pass