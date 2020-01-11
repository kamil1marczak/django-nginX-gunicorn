# django-nginX-gunicorn 


REQUIREMENTS:
git, nginX, docker, docker-compose, postgres, python3, django, cron, crontab


MANUAL:

1) install postgres:
sudo apt-get install postgresql

set up login and password in postgres

in case you choose other while instaling postgress remember to change USER and PASSWORD in settings.py in DATABASES section

2) set up db name, engine, user, password, host and port for application in Dockerfile, default are:

ENV DB_NAME weather
ENV ENGINE ***
ENV DB_USER ***
ENV DB_PASSWORD ***
ENV HOST_ON_SERVER ***
ENV PORT_ON_SERVER ***


3) create database in accordance to DB_NAME

A) initial deployment and restructuring models:
execute: initial_deployment.sh

choose superuser credentials, default are:
ENV SUPERUSER ***
ENV SU_PASSWORD ***
ENV SU_EMAIL ***


B) to run app:
choose SSL or no SSL mode, default is:
ENV SSL_CHECK False

Build code with docker compose: docker-compose build
Run the built container: docker-compose up -d

C) to run stanalone script execute: python_for_cron.sh

cron set up enter cron folder, to add crontab list, execute: crontab cron.txt
to start set up cron: service cron start
to stop cron: service cron stop
to check if running:
service cron status


** to add new users enter url path /initial_user/ or you can manage it from admin view /admin/
(/admin/ have right to delete user from /initial_user/ you can only add one)










