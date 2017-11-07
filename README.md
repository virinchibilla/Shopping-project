# Shopping (mini project)

## Introduction

Welcome to the codebase for the Shopping project. 

The front-end uses [Vue.js](https://vuejs.org), with help of [webpack](https://webpack.js.org) and [yarn](https://yarnpkg.com/en/). 

The back-end uses [Django REST framework](http://www.django-rest-framework.org) with [PostgreSQL](https://www.postgresql.org) as the database.

## Prerequisites

Docker, along with docker-compose, is used to manage the dependencies of this project. 

To install docker, download it from [here](https://www.docker.com/products/docker) (docker-compose should be installed along with the process).


## Get started

First go to the Shopping project Folder( cd miniproject)


To get a list of helper commands:

```bash
$ source project.sh
```

Then you will get access to the following commands:

- To bootstrap the project: `$ build-stack`
- To run the project: `$ start-stack`
- To display real-time logs: `$ logs`
- To stop the project: `stop-stack`
- To create new migrationfiles: `db-make-migrations`
- To run a database migration: `db-migrate`
- To create a django superuser: `create-su`
- To run tests for the backend: `test-backend`
- To run tests for the frontend: `test-frontend`
- To build the production: `build-production`
- To fix sass packages: `fix-sass`
- To fix problem in backend: `fix-start-stack`


-> Steps to follow:

After running stack
If there is any problem with 'db backend' 

connect to the db docker postgres image --> docker exec -it $(docker ps -qf "name=miniproject_db_1")  bash

 run 'psql -U postgres' then run: 

drop database backend;
CREATE DATABASE "backend"
    WITH OWNER "postgres"
    ENCODING 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE template0;

    \q
    exit

db-make-migrations
db-migrate
fix-sass
restart-stack
fix-start-stack




1. Inorder to interact with django Rest framework. First create django superuser by typing `create-su` and then go to http://127.0.0.1:8000/admin/ 

2. Log into `http://127.0.0.1:8080/?#/` in the web brwoser to interact with the shopping project.


## Collaboration

For details on using github, please visit the [sysbio wiki](http://wiki.sysbio.chalmers.se/mediawiki/index.php/Development_guidelines#Github).