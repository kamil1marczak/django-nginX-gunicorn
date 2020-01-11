# django-nginX-gunicorn 


REQUIREMENTS: <br>
git, nginX, docker, docker-compose, postgres, python3, django, cron, crontab <br>


MANUAL: <br>

1) install postgres:
sudo apt-get install postgresql <br>

set up login and password in postgres <br>

in case you choose other while instaling postgress remember to change USER and PASSWORD in settings.py in DATABASES section <br>

2) set up db name, engine, user, password, host and port for application in Dockerfile, default are: <br>

ENV DB_NAME weather <br>
ENV ENGINE *** <br>
ENV DB_USER *** <br>
ENV DB_PASSWORD *** <br>
ENV HOST_ON_SERVER *** <br>
ENV PORT_ON_SERVER *** <br>


3) create database in accordance to DB_NAME <br>

A) initial deployment and restructuring models:
execute: initial_deployment.sh <br>

choose superuser credentials, default are:
ENV SUPERUSER *** <br>
ENV SU_PASSWORD *** <br>
ENV SU_EMAIL *** <br>


B) to run app:
choose SSL or no SSL mode, default is:
ENV SSL_CHECK False

Build code with docker compose: docker-compose build
Run the built container: docker-compose up -d

C) to run stanalone script execute: python_for_cron.sh

cron set up enter cron folder, to add crontab list, execute: crontab cron.txt
to start set up cron: service cron start <br>
to stop cron: service cron stop <br>
to check if running:
service cron status

<br>

** to add new users enter url path /initial_user/ or you can manage it from admin view /admin/ 
(/admin/ have right to delete user from /initial_user/ you can only add one)










