FROM python:3.6

RUN mkdir src
RUN cd src
RUN pip install pipenv && pipenv install --system


COPY city_weather /src/








