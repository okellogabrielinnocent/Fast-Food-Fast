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