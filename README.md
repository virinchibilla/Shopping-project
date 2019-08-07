# Shopping (mini project)

## Introduction

Welcome to the codebase for the Shopping project. 

The front-end uses [Vue.js](https://vuejs.org), with help of [webpack](https://webpack.js.org) and [yarn](https://yarnpkg.com/en/). 

The back-end uses [Django REST framework](http://www.django-rest-framework.org) with [PostgreSQL](https://www.postgresql.org) as the database.

This is a mini application with the theme e-commerce shopping website.
First you will sign up as a new user and then you sign in.
After sign in you will get access to buy products and every product that you buy you will get invoice.
You can also change role permissions of users who are registered.

## Prerequisites

Docker, along with docker-compose, is used to manage the dependencies of this project. 

To install docker, download it from [here](https://www.docker.com/products/docker) (docker-compose should be installed along with the process).


## Get started

First go to the Shopping project Folder( cd Shopping-project)


To get a list of helper commands:

```bash
$ source project.sh
```

Then you will get access to the following commands:

- To bootstrap the project: `$ build-stack`
- To run the project: `$ start-stack`
- To display real-time logs: `$ logs`
- To stop the project: `stop-stack`
- To stop and run the project: `restart-stack`
- To create new migrationfiles: `db-make-migrations`
- To run a database migration: `db-migrate`
- To create a django superuser: `create-su`
- To run tests for the backend: `test-backend`
- To build the production: `build-production`
- To fix sass packages: `fix-sass`
- To fix problem in backend: `fix-start-stack`


## Build & run the project:
```
$ build-stack
```
```
$ start-stack
```
```
$ database-generate-migrate 
```
```
$ create-su 
```
```
$ fix-start-stack
```


1. Inorder to interact with django Rest framework (Backend). First create django superuser by typing `create-su` and then go to http://localhost:8000/admin/

2. Log into http://localhost://8080/#/ or http://127.0.0.1:8080/?#/ in the web brwoser to interact with the shopping project.

3. To buy product items, first add items and their prices manually in the django Rest framework.

4. First, fill your address in the browser inorder to get invoices for the products that you buy.

5. To change roles of users, you can change it under Apiusers section in django.

## Collaboration

For details on using github, please visit the [sysbio wiki](http://wiki.sysbio.chalmers.se/mediawiki/index.php/Development_guidelines#Github).