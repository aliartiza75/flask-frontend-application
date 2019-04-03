# This version of sw-base has kudu package installed in it
FROM ubuntu:16.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt install -y curl 

LABEL "MAINTAINER"="aliartiza75@yahoo.com"
LABEL "DESCRIPTIONS"="Dockerfile for the Frontend service"

# app directory for application containing code files
WORKDIR /usr/src/datetime

# copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
# copying kudu service specific files and folders to worker directory
COPY . .

EXPOSE 5001
CMD export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && flask run --host=$FLASK_HOST_IP --port=$((FLASK_HOST_PORT))


