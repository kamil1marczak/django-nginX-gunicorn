# Generated by Django 3.0.2 on 2020-01-15 17:09

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=256, unique=True)),
                ('latitude_deg', models.DecimalField(decimal_places=15, max_digits=50)),
                ('longitude_deg', models.DecimalField(decimal_places=15, max_digits=50)),
                ('country', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherArchive',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('last_update_timestamp', models.DateTimeField()),
                ('weather', django.contrib.postgres.fields.jsonb.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.Cities', to_field='name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='ApiKeys',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
