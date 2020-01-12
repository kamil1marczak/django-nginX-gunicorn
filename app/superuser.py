import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = "flight_analyser.settings"
django.setup()

from django.contrib.auth.models import User
if User.objects.filter(username='superuser'):
    pass
else:
    User.objects.create_superuser(os.getenv('SUPERUSER', default='superuser'), os.getenv('SU_EMAIL', default='user@user.com'), os.getenv('SU_PASSWORD', default='adminpass'))



