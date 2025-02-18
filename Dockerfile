# syntax=docker/dockerfile:1
FROM ubuntu:22.04
COPY . /app
RUN apt-get -y update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev &&\
    pip install -r /app/requirements.txt
ENTRYPOINT ["python3", "/app/start-spider.py"]
