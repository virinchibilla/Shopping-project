FROM node
RUN npm cache clean --force
RUN npm install webpack -g

ADD . /project
WORKDIR /project

RUN npm build

EXPOSE 8080