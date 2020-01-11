import requests
import json
from city_weather.settings import *


# alternativeAIP
# url = "https://community-open-weather-map.p.rapidapi.com/weather"
#
# querystring = {"lat": lat, "lon": lon, "id": "2172797", "units": "%22metric%22"}
#
# headers = {
#     'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
#     'x-rapidapi-key': "ce30d525famsh578de54863cebf1p1400a2jsn7201f44d01b2"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
# weather_data = response.text

class WeatherApi:
    @staticmethod
    def connect_to_api(lat, lon):


        url = f"{API_weather}/data/2.5/weather?lat={lat}&lon={lon}&APPID={weather_api_key}&units=metric"
        response = requests.request('GET', url)

        weather_data = json.loads(response.text)

        return weather_data

    @staticmethod
    def weather_json_restructure(lat, lon):
        weather_data = WeatherApi.connect_to_api(lat, lon)

        weather_data['main']['temp'] = str(int(weather_data['main']['temp'])) + '°C'
        weather_data['main']['temp_min'] = str(int(weather_data['main']['temp_min'])) + '°C'
        weather_data['main']['temp_max'] = str((weather_data['main']['temp_max'])) + '°C'
        weather_data['wind']['speed'] = str((weather_data['wind']['speed'])) + 'm/s'
        weather_main = weather_data['main']
        weather_icon = "http://openweathermap.org/img/wn/" + weather_data['weather'][0]['icon'] + "@2x.png"
        weather_desc = weather_data['weather']
        weather_wind = weather_data['wind']['speed']

        return {'weather_data': weather_data,
                'weather_main': weather_main,
                'weather_desc': weather_desc,
                'weather_icon': weather_icon,
                'weather_wind': weather_wind}


# exaple data from Weather API
"""
{"coord": {"lon": -101.47, "lat": 37.7},
  "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}], "base": "stations",
  "main": {"temp": 268.62, "pressure": 1011, "humidity": 86, "temp_min": 267.15, "temp_max": 270.15},
  "visibility": 16093, "wind": {"speed": 2.1, "deg": 270}, "clouds": {"all": 1}, "dt": 1575552384,
  "sys": {"type": 1, "id": 4594, "country": "US", "sunrise": 1575553562, "sunset": 1575588434}, "timezone": -21600,
  "id": 5446683, "name": "Ulysses", "cod": 200})
{'lat': '37.704022', 'lon': '-101.473911', 'callback': 'weather', 'id': '2172797', 'units': '%22metric%22'}
"""
