"""api views"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity,
create_access_token,get_jwt_claims)
from app.model.order import Orders
from app.model.users import User
from app.model.validation import Validations
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
        admin = request.json['admin']
        
        
        print("===data==",username,email,admin,address,password)

        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", username):
            return jsonify({"message":"Username can not be empty"}), 400
        if  re.search("[0-9]", username):
            return jsonify({"message":"Username can not numbers"}), 400
        
        if users.validate_user_duplicate(username, password, address,
                email, admin) is True:
                return jsonify({"message": "Email is already existing"}), 409

        users.sign_up(username, password, address, email, admin)
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
        username = data['username']
        password = data['password']
        access_token = users.user_login(username, password)
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
        return jsonify({"message": "Item created successfuly","Item":data}), 201
        
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
        token_owner = token_owner["user_id"]
        if token_owner !=  token_owner["user_id"]:
            return jsonify({"Only user who place order can view it"}), 403
        
        result = orders.get_order_list()
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
        if token_owner['admin'] == True:
            result = orders.get_order_list()
            if result is None:
                return jsonify({'message':'Order does not exist'}), 200
        
            return jsonify({"Orders": result}), 200
        return jsonify({'message':'Only an admin can access all orders'}), 403

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
    """view to update an order"""
    
    try:
        data = request.get_json()
        token_owner = get_jwt_identity()
        data["user_userid"] = token_owner["user_id"]        
        data = orders.update_order(data["user_userid"],data["orderid"],data["order_status"])
        return jsonify({"message": "Order updated successfuly"}), 200
        
    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response