"""api views"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity,create_access_token
from app.model.order import Orders
from app.model.users import User
from app.model.validation import Validations
from datetime import date
import re


ROUTES = Blueprint('routes', __name__)
users = User()
orders = Orders()


@ROUTES.route('/API/v1/auth/user/signup', methods=['POST'])
def create_user():
    """ Creating a user account
    calls the signup() function in models.py
    """    
    try:
        email = request.json['email']
        admin = request.json['admin']
        username = request.json['username']
        address = request.json['address']
        password = request.json['password']

        # if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", username, password):
        #     return jsonify({"message":"invalid password data"}), 404
        
        if users.validate_user_duplicate(username, password, address,
                email, admin) is True:
                return jsonify({"message": "Username is already existing"}), 409

        users.sign_up(username, password, address, email, admin)
        return jsonify({"message": "User registeration successfuly"}), 201

    except Exception as err:
        return jsonify({"message": "The {} field is missing".format(str(err))}), 404

@ROUTES.route('/API/v1/auth/login', methods=['POST'])
def login():

    try:
        data = request.get_json()
        info = users.user_login(data["username"], data["password"])
        return info
    except Exception as err:
        return jsonify({"message": "The {} field is missing".format(str(err))}), 404

@ROUTES.route('/API/v1/menu', methods=['POST'])
@jwt_required
def add_item_to_menu():
    """ Creating a user account
    calls the signup() function in models.py
    """
      
    try:
        data = request.get_json()
        token_owner = get_jwt_identity()
        data["user_userid"] = token_owner["user_id"]
        description = request.json['description']
        price = request.json['price']

        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", description, price):
            return jsonify({"message":"Input fields should not be empty"}), 404

        if orders.validate_item_creation(description, price, data["user_userid"]) is True:
            return jsonify({"message": "Item already existing"}), 409

        orders.create_item(description, price, data["user_userid"])
        return jsonify({"message": "Item created successfuly"}), 201
        
    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/menu', methods=['GET'])
def get_avialable_menu():
    """ Get all menu items
    This function returns all the items in the menu
    It calls the get_menu_list function in models.order.py module
    """
    try:
        result = orders.get_menu_list()
        return jsonify({"Avialable menu": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response
    
@ROUTES.route('/API/v1/users/orders', methods=['POST'])
def place_order():
    """ Placing order
    calls the create_order and check_if_order_exist function in models.py
    """
      
    try:
        today = str(date.today())
        data = request.get_json()
        data['date'] = today
        orderid = request.json['orderid']
        user_userid = request.json['user_userid']
        description = request.json['description']
        menu_menuid = request.json['menu_menuid']

        if not re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", description):
            return jsonify({"message":"Input fields should not be empty"}), 404

        if orders.check_if_order_exist(orderid, data['date'],menu_menuid, user_userid) is True:
            return jsonify({"message": "Order is already existing"}), 409

        orders.create_order(data['date'],menu_menuid, user_userid)
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
        data = request.get_json()
        token_owner = get_jwt_identity()
        data["user_userid"] = token_owner["user_id"]
        result = orders.get_order_list()
        return jsonify({"Orders": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response

@ROUTES.route('/API/v1/orders', methods=['GET'])
@jwt_required
def get_all_orders():
    """ Getting orders
    calls the create_order and check_if_order_exist function in models.py
    """
      
    try:
        data = request.get_json()
        token_owner = get_jwt_identity()
        data["user_userid"] = token_owner["user_id"]
        if data["user_userid"] is not 'True':
            return jsonify({"UNAUTHORIZED Access. Only admin is allowed"}), 401
        result = orders.get_order_list()
        return jsonify({"Orders": result}), 200

    except Exception as err:
        response = jsonify({"Error": "The {} parameter does not exist".format(str(err))}), 400
        return response