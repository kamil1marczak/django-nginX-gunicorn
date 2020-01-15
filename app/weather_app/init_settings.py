from django.contrib.auth.models import User
from weather_app.models import ApiKeys
from django.db import connection
from core.settings import BASE_DIR
import os
from random import randint


class UserManagement:
    @staticmethod
    def change_password(user: str, password: str):
        u = User.objects.get(username=user)
        u.set_password(password)
        u.save()

    @staticmethod
    def create_user(user: str, mail: str, passw: str):
        user = User.objects.create_user(user, mail, passw)
        user.save()
        ApiKeys.objects.create(api_key=randint(100000, 999999), user=user)


class TablePopulator:

    def city_list():
        with connection.cursor() as cursor1:
            sql = open(os.path.join(BASE_DIR, 'SQL/cities_dataset.txt')).read()
            cursor1.execute(sql)
