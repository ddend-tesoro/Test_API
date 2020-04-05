FROM python:3.7-alpine
MAINTAINER Grigory G

#ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

ADD . /app

CMD python manage.py runserver 0.0.0.0:8000


