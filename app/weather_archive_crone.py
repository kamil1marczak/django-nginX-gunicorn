import os
import django
from urllib import request

os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"
django.setup()

from weather_app.weather_archive import WeatherArchiveCreator

target_data = [{'city': 'Warsaw'},
               {'city': 'Poznań'},
               {'city': 'Wrocław'},

               ]

for i in target_data:
    WeatherArchiveCreator.save_to_weather_archive(i['city'])


        # def city_name_weather()
        # cities_data = Cities.objects.get(name=name)
        # lat = cities_data.latitude_deg
        # lon = cities_data.longitude_deg
        # weather_data_context = WeatherApi.weather_json_restructure(lat, lon)
        #
        # def foo:
        # weather = city_name_weather(name)
        # WeatherArchive.objects.create(last_update_timestamp=datetime.now() + timedelta(hours=1), city=Cities.objects.get(name=name), weather=weather)



# bash to set up script every 30 minutes:
#     */30 * * * * python3 path/to/script >dev/null 2?&1
# to check if running:
#     tail -f /var/log/syslog | grep -i cron
