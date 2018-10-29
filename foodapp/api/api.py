"""api views"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity,
create_access_token,get_jwt_claims)
from foodapp.model.order import Orders
from foodapp.model.users import User
from foodapp.model.validation import Validations
from datetime import datetime
# from flasgger import Swagger, swag_from
import re


ROUTES = Blueprint('routes', __name__)
users = User()
orders = Orders()
validations = Validations


@ROUTES.route('/API/v1/auth/user/signup', methods=['POST'])
# @swag_from('../Docs/signup.yml')
def create_user():
    """ Creating a user account
    calls the signup() function in models.py
    """    
    try:
        
        username = request.json['username'].strip()
        password = request.json['password'].strip()
        address = request.json['address'].strip()
        email = request.json['email'].strip()

        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", username):
            return jsonify({"message":"Username can not be empty"}), 400
        if  re.search("[0-9]", username):
            return jsonify({"message":"Username can not numbers"}), 400
        
        if users.validate_user_duplicate(username, password, address,
                email) is True:
                return jsonify({"message": "Email is already existing"}), 409

        users.sign_up(username, password, address, email)
        return jsonify({"message": "User registered successfuly"}), 201

    except Exception as err:
        return jsonify({"message": "The {} field is missing".format(str(err))}), 400

@ROUTES.route('/API/v1/auth/login', methods=['POST'])
# @swag_from('../Docs/login.yml')
def login():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'Message': 'Data passed should be in JSON format!'}), 400
        email = data['email']
        password = data['password']
        access_token = users.user_login(email, password)
        if access_token is not None:
            return jsonify({"Message": "Login successful",
                                    "Token": access_token})
        return jsonify({'message':'Invalid password or username'}), 400  
    except KeyError:
        return jsonify({'message': 'Missing key parameter: username, password'}), 400

@ROUTES.route('/API/v1/menu', methods=['POST'])
@jwt_required
def add_item_to_menu():
    """ Creating a user account
    calls the signup() function in models.py
    """
      
    try:
        data = request.get_json()
        token_owner = get_jwt_identity()
        '''This line get userid from token'''
        data["user_userid"] = token_owner["user_id"]
        description = request.json['description']
        price = request.json['price']

        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", description, price):
            return jsonify({"message":"Input fields should not be empty"}), 400

        if orders.validate_item_creation(description, price, data["user_userid"]) is True:
            return jsonify({"message": "Item already existing"}), 409

        orders.create_item(description, price, data["user_userid"])
        return jsonify({"message": "Item created successfuly"}), 201
        
    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/menu', methods=['GET'])
@jwt_required
def get_avialable_menu():
    """ Get all menu items
    This function returns all the items in the menu
    It calls the get_menu_list function in models.order.py module
    """
    try:
        token_owner = get_jwt_identity()
        result = orders.get_menu_list()
        return jsonify({"Avialable menu": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/users/orders', methods=['POST'])
@jwt_required
def place_order():
    """ Placing order
    calls the create_order and check_if_order_exist function in models.py
    """
      
    try:
        today = str(datetime.now())
        data = request.get_json()
        token_owner = get_jwt_identity()
        '''get user id from token'''
        data["user_userid"] = token_owner["user_id"]
        order_date = today

        orders.create_order(order_date, data["user_userid"], data["food_item_itemid"], data["quantity"])
        return jsonify({"message": "Order placed successfuly"}), 201
        
    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/users/orders', methods=['GET'])
@jwt_required
def get_orders():
    """ Getting orders for a particular user
    calls the create_order and check_if_order_exist function in models.py
    """
      
    try:
        token_owner = get_jwt_identity()
        result = orders.get_order_list()
        if len(result)==0:
            return jsonify({'message': 'Your order history is empty. Please make orders!'}), 404
        return jsonify({"Orders": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response


@ROUTES.route('/API/v1/orders', methods=['GET'])
@jwt_required
def get_all_orders():
    """ Getting orders for a particular user
    calls the create_order and check_if_order_exist function in models.py
    """
      
    try:
        token_owner = get_jwt_identity()
        result = orders.get_order_list()
        return jsonify({"Orders": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/orders/<orderid>', methods=['GET'])
@jwt_required
def get_order_by_id(orderid):
    """ Getting orders for a particular user
    Retrieves a single order by providing the orderid """
    try:
        token_owner = get_jwt_identity()
        result = orders.order_details(orderid)
        if not result:
            raise Exception
        return jsonify({"Your order": result}), 200
        
    except:
        return jsonify({"Message": "The order with order id {} does not exist".format(orderid)}), 404


@ROUTES.route('/API/v1/orders/<orderid>',methods=['PUT'])
@jwt_required
def update_orders(orderid):
    token_owner = get_jwt_identity()
    # if token_owner['admin'] == True:
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON format!'}), 400
        else:
            valid_status = ['Accepted','Complete', 'Processing', 'Cancelled']            
            if data["order_status"] not in valid_status:
                return ('Invalid status')

        status = data['order_status']
        result = orders.update_order(orderid, status)
        return jsonify({'Updated_order': result})
    except:
        return jsonify({"Message": "The order with order id {} does not exist".format(orderid)}), 404