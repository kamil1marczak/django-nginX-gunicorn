from django.core.wsgi import get_wsgi_application
import os
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_analyser.settings')
application = get_wsgi_application()

# testing data in AirportsAllData
from acb.models import AirportsAllData

@pytest.mark.django_db
def test_AirportsAllData_model(airports_all_data_single_object_test):
    assert len(AirportsAllData.objects.all()) == 1
    assert AirportsAllData.objects.get(name='Kugluktuk Airport') == airports_all_data_single_object_test

