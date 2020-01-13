# city weather monorepo 


REQUIREMENTS: <br>
git, docker, docker-compose, postgres, python3, cron, crontab <br>

<h2> app diagram </h2>

![app diagram](city_weather_diagram.png)


<br> 


<h2> instalation </h2> <br>

<h3> create .env, populate it with env as presented in points below, than place file in main folder </h3>

<h3> 1) install postgres: </h3>
apt-get install postgresql <br>

set up login and password in postgres <br>

in case you choose other while instaling postgress remember to change USER and PASSWORD in settings.py in DATABASES section <br>

<H3> 2) set up db name, engine, user, password, host and port for application .env, </h3> <br> 
default are: <br>

ENV DB_NAME weather <br>
ENV ENGINE *** <br>
ENV DB_USER *** <br>
ENV DB_PASSWORD *** <br>
ENV HOST_ON_SERVER *** <br>
ENV PORT_ON_SERVER *** <br>


<h3> 3) create database name in accordance to DB_NAME </h3> <br>

<h4> A) initial deployment and restructuring models: </h4>
execute: bash etc/initial_deployment.sh <br>

choose superuser credentials, and write them in .env: <br>
ENV SUPERUSER *** <br>
ENV SU_PASSWORD *** <br>
ENV SU_EMAIL *** <br>


<h4> B) to run app: </h4>
choose SSL or no SSL mode, wtite in .env as example: <br>
ENV SSL_CHECK False
<br>
Build code with docker compose: docker-compose build <br>
Run the built container: docker-compose up -d 

<h4> C) to run stanalone script </h4>

execute: bash ect/python_for_cron.sh

cron set up enter cron folder, to add crontab list, execute: crontab cron.txt
to start set up cron: service cron start <br>
to stop cron: service cron stop <br>
to check if running:
service cron status

<br>

** to add new users enter url path /initial_user/ or you can manage it from admin view /admin/ 
(/admin/ have right to delete user from /initial_user/ you can only add one)










