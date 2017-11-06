FROM python:3.5
ENV PYTHONUNBUFFERED 1

ARG DEBIAN_FRONTEND=noninteractive


RUN mkdir /project
WORKDIR /project

ADD requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt

ADD . /project
