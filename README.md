[![Build Status](https://travis-ci.com/okellogabrielinnocent/Fast-Food-Fast.svg?branch=challenge2-api)](https://travis-ci.com/okellogabrielinnocent/Fast-Food-Fast) 
[![Coverage Status](https://coveralls.io/repos/github/okellogabrielinnocent/Fast-Food-Fast/badge.svg?branch=challenge2-api)](https://coveralls.io/github/okellogabrielinnocent/Fast-Food-Fast?branch=challenge2-api)

## Project Overview
Fast-Food-Fast is a food delivery service app for a restaurant.

### Git pages link
https://okellogabrielinnocent.github.io/Fast-Food-Fast/

### Heroku link
https://fast-foot-fast.herokuapp.com/api/v1/orders

**API end points**

EndPoint | Functionality
----------------------- | -------------
POST /api/v1/orders|Place a new order for food.
GET /api/v1/orders | Get a list of orders.
GET /api/v1/orders/<order_id>|Fetch a specific order.
PUT /api/v1/orders/<order_id>|Update the order status.



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

> Post Order https://fast-foot-fast.herokuapp.com/api/v1/orders

      { "description":"Rice and Chicken",
        "client":"Gabriel",
        "location":"Kisaasi",
        "quantity":"4"
      }

>Get a list of orders https://fast-foot-fast.herokuapp.com/api/v1/orders

            {
            "Orders": [
                  {
                        "Order": {
                        "Orderd_At": "2018-09-26 15:40:06.100573",
                        "client": "Gabriel",
                        "description": "Rice and Chicken",
                        "id": "1",
                        "location": "Kisaasi",
                        "quantity": "4",
                        "status": "Pending"
                              }
                  }
            ]
            }

>Fetch a specific order.https://fast-foot-fast.herokuapp.com/api/v1/orders/1

            {
            "Your order": [
                  {
                        "Orderd_At": "2018-09-26 15:40:06.100573",
                        "client": "Gabriel",
                        "description": "Rice and Chicken",
                        "id": "1",
                        "location": "Kisaasi",
                        "quantity": "4",
                        "status": "Pending"
                  }
            ]
            }



>Update the order status.https://fast-foot-fast.herokuapp.com/api/v1/orders/1

      {
      "message": [
            {
                  "Orderd_At": "2018-09-26 15:40:06.100573",
                  "client": "Gabriel",
                  "description": "Rice and Chicken",
                  "id": "1",
                  "location": "Kisaasi",
                  "quantity": "4",
                  "status": "Rejected"
                  
            }
      ]
      }
