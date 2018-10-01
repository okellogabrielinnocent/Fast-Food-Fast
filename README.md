[![Build Status](https://travis-ci.org/okellogabrielinnocent/Fast-Food-Fast.svg?branch=challeng3-api)](https://travis-ci.org/okellogabrielinnocent/Fast-Food-Fast) 
[![Coverage Status](https://coveralls.io/repos/github/okellogabrielinnocent/Fast-Food-Fast/badge.svg?branch=challeng3-api)](https://coveralls.io/github/okellogabrielinnocent/Fast-Food-Fast?branch=challenge2-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/07b8e72796f0cc9c1a30/maintainability)](https://codeclimate.com/github/okellogabrielinnocent/Fast-Food-Fast/maintainability)

## Project Overview
Fast-Food-Fast is a food delivery service app for a restaurant.

### Git pages link
https://okellogabrielinnocent.github.io/Fast-Food-Fast/

### Heroku link
https://fast-foot-fast.herokuapp.com/api/v1/orders

**API end points**

EndPoint|Functionality|Note
------|-------|------
POST /auth/signup |Register a user|
POST /auth/login|Login a user|
POST /users/orders|Place an order for food.|
GET /users/orders|Get the order history for a particular user.|
GET /orders/|Get all orders|Only Admin (caterer) should have access to this route
GET /orders/<orderId>|Fetch a specific order|Only Admin (caterer) should have access to this route
PUT /orders/<orderId>|Update the status  of an order|Only Admin (caterer) should have access to this route. The Status  of an order could either be New, Processing, Cancelled or Complete.
GET /menu|Get available menu|
POST /menu|Add a meal option to the menu.|Only Admin (caterer) should have access to this route



**Tools Used**
- Server-Side Framework: Flask Python Framework

- Linting Library: Pylint, a Python Linting Library

- Style Guide: PEP8 Style Guide

- Testing Framework: <PyTest, a Python Testing Framework>

**Prerequisites**

Below are the things you need to get the project up and running.

- git : To update and clone the repository
- python3: Language used to develop the api
- pip: A python package used to install project requirements specified in the requirements text file.
- Database: PostgreSQL


**Installing the project**

Clone: 
        
       "https://github.com/okellogabrielinnocent/Fast-Food-Fast.git"
  in the terminal or git bash or command prompt.

To install the requirements. run:

      pip install -r requirements.txt

cd to the folder fasts food fast
And from the root of the folder, type:
      
      python run.py
      
To run the tests and coverage, from the root folder, type: 
        
        pytest -v --cov

### Required Features

>Create user accounts that can signin/signout from the app.

>Place an order for food.

>Get list of orders.

>Get a specific order.

>Update the status of an order.

>Get the menu.

>Add food option to the menu.

>View the order history  for a particular user.
