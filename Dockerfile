
pull base image.
FROM python:3.4.5-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  make \
  gcc \
  python3-dev \
  mmongodb

RUN mkdir /opt/pets-api

WORKDIR /opt/pets-api

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python manage.py runserver
