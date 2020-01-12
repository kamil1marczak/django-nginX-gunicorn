import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"
django.setup()

from weather_app.models import Cities
from weather_app.init_settings import TablePopulator

if Cities.objects.filter(name='Warsaw'):
    pass
else:
    TablePopulator.city_list()
