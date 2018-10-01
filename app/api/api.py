"""api views"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.model.order import Orders
from app.model.users import User


ROUTES = Blueprint('routes', __name__)
users = User()

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
        result = users.sign_up(username, password, address, email, admin)

        return result
    except Exception as err:
        return jsonify({"message": "The {} parameter does not exist".format(str(err))}), 400

@ROUTES.route('/API/v1/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        # info = Validate.validate_login(data["username"], data["password"])
        # if info is True:
        obj = User()
        info = obj.login(data["username"], data["password"])
        return info
        # else:
        #     return jsonify({"message": """Bad username or empty password field"""}), 400

    except:
        return jsonify({"Error": "Should have a username field taking in a string and password field taking in a string"}), 400