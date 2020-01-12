import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"
django.setup()

from weather_app.models import Countries
from weather_app.init_settings import TablePopulator

if Countries.objects.filter(name='Poland'):
    pass
else:
    TablePopulator.city_list()
