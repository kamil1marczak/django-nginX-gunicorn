import os
import django
from urllib import request


os.environ['DJANGO_SETTINGS_MODULE'] = "flight_analyser.settings"
django.setup()

from acb.flights_archive import FlightArchive


delay_selector = '{"status":"active","isDelay":"delay"}'
canceled_selector = '{"status":"canceled","isDelay":"notDelay"}'

target_data = [{'airport_selector': 'WAW', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'WAW', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'WMI', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'WMI', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'KRK', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'KRK', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'KTW', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'KTW', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'GDN', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'GDN', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'WRO', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'WRO', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'POZ', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'POZ', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},
               {'airport_selector': 'BZG', 'type_selector': 'departure', 'canceled_deleyed_selector': delay_selector},
               {'airport_selector': 'BZG', 'type_selector': 'departure', 'canceled_deleyed_selector': canceled_selector},

               ]


for i in target_data:
    try:
        FlightArchive.save_to_flight_archive(i['airport_selector'], i['type_selector'], i['canceled_deleyed_selector'])
    except:
        pass


# type = ['departure', 'arrival' ]
# status = ['active', 'canceled']
# isDelay = ['delay', 'notDelay']
# airport = [iata code]
# '{"status":"active","isDelay":"delay"}'
# '{"status":"canceled","isDelay":"notDelay"}'


# bash to set up script every 30 minutes:
#     */30 * * * * python3 path/to/script >dev/null 2?&1
# to check if running:
#     tail -f /var/log/syslog | grep -i cron