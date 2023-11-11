import requests
from datetime import datetime
import json
def get_weather_info(city):
    MY_KEY ='You token'

    URL = f'https://api.openweathermap.org/data/2.5/weather'
    PARAMETERS = {
        'q': city,
        'appid': MY_KEY
       }
    KELVIN = 273.15
    res = requests.get(URL, params=PARAMETERS).json()
    temp = round(res['main']['temp'] - KELVIN, 2)
    timezone = res['timezone']
    weather = res['weather'][0]['main']
    sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + timezone).strftime('%H:%M:%S %D-%M-%Y')
    sunrset = datetime.utcfromtimestamp(res['sys']['sunset'] + timezone).strftime('%H:%M:%S %D-%M-%Y')
    wind = res['wind']['speed']

    print(f"""Siz kritgan:🏙 {city.title()} da
Havo harorati:🌡 {temp} selsiyada
Ob-Havo:🌤 {weather}
Quyosh chqishi:🌅 {sunrise}
Quyosh botidhi:🌅 {sunrset}
Shamol tezligi:💨 {wind} m/s""")

while True:
    print('------------------------------------------')
    city = input('Qaysi shaxarni qidiryapsiz:').lower()
    if city == 'stop':
        break
    try:
       get_weather_info(city)
    except KeyError:
        print('Bunday shaxar topilmadi qayta urinib koring!')
    except Exception as p:
        print(p.__class__)













