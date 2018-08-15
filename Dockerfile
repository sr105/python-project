FROM python:3.6-alpine3.7

MAINTAINER "Hivelocity"
LABEL project="core.hivelocity.net"
LABEL version = "1.0.0"
LABEL author="Zach Kazanski"
LABEL author_email="kazanski.zachary@gmail.com"

#### BASIC CONFIGURATION STUFF ####

RUN apk add --update --no-cache \
    py-pip \
    bind-tools \
    bash

RUN mkdir /app
ADD requirements.txt /app/
RUN pip --no-cache-dir install --retries=1 --timeout=30 -r /app/requirements.txt
ADD . /app/
# ENV PYTHONPATH /app:src/

CMD sleep 3000
