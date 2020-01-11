FROM ubuntu:18.04

RUN apt update
RUN apt-get install cron
RUN apt install -y python3-pip 
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install django django-tinymce4-lite
RUN pip3 install psycopg2-binary requests tablib virtualenv gunicorn
RUN mkdir src
RUN cd src
RUN virtualenv djangomachine

RUN mkdir /var/www


ENV DB_NAME weather
ENV ENGINE ***
ENV DB_USER ***
ENV DB_PASSWORD ***
ENV HOST_ON_SERVER ***
ENV PORT_ON_SERVER ***
ENV DEBUG True

ENV SUPERUSER ***
ENV SU_PASSWORD ***
ENV SU_EMAIL ***

ENV SSL_CHECK False

COPY city_weather /src/








