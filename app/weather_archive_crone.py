import os
import django
from urllib import request

os.environ['DJANGO_SETTINGS_MODULE'] = "city_weather.settings"
django.setup()

from weather_app.weather_archive import WeatherArchiveCreator

target_data = [{'city': 'Warsaw'},
               {'city': 'Poznań'},
               {'city': 'Wrocław'},

               ]

for i in target_data:
    WeatherArchiveCreator.save_to_weather_archive(i['city'])




# bash to set up script every 30 minutes:
#     */30 * * * * python3 path/to/script >dev/null 2?&1
# to check if running:
#     tail -f /var/log/syslog | grep -i cron
