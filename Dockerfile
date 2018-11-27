
#pull base image.
FROM python:3.4.5-slim


RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 58712A2291FA4AD5


RUN apt-get update && apt-get install -y --force-yes \
  build-essential \
  make \
  gcc \
  python3-dev \
  mongodb-org=3.6.9


RUN systemctl enable mongod.service
RUN systemctl start mongod
RUN systemctl status mongod

RUN mkdir /opt/pets-api

WORKDIR /opt/pets-api

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python manage.py runserver
