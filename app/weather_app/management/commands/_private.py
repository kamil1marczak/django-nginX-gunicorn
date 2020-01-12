
from weather_app.models import Cities
from django.contrib.auth.models import User
from django.db import connection
from core.settings import BASE_DIR
import os

def populate_cities():
    if Cities.objects.filter(name='Warsaw'):
        pass
    else:
        with connection.cursor() as cursor1:
            sql = open(os.path.join(BASE_DIR, 'SQL/cities_dataset.sql')).read()
            cursor1.execute(sql)

def create_super_user():
    if User.objects.filter(username=os.getenv('SUPERUSER', default='superuser')):
        pass
    else:
        User.objects.create_superuser(os.getenv('SUPERUSER', default='superuser'), os.getenv('SU_EMAIL', default='user@user.com'), os.getenv('SU_PASSWORD', default='adminpass'))



