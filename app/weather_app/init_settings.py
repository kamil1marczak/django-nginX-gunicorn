from django.contrib.auth.models import User
from django.db import connection
from core.settings import BASE_DIR
import os


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


class TablePopulator:

    def city_list():
        with connection.cursor() as cursor1:
            sql = open(os.path.join(BASE_DIR, 'SQL/cities.sql'), encoding='utf-8', errors='replace').read()
            cursor1.execute(sql)
