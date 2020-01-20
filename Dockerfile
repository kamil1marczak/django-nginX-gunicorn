FROM python:3.6

RUN mkdir src
RUN cd src
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt

COPY app /src/
COPY etc/SQL /src/








