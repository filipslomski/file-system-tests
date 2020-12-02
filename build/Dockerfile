FROM python:3.8

LABEL description="Install environment for python testing framework."
RUN apt-get update
COPY build/requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get install -y build-essential
RUN apt-get install zip
WORKDIR /var/www/
