from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

App = Flask(__name__)
App.config['JWT_SECRET_KEY'] = 'innocorp'
jwt = JWTManager(App)
'''JWT MAnager
An object used to hold JWT settings and callback functions
for the Flask-JWT-Extended extension.'''

from app.api.api import ROUTES
App.register_blueprint(ROUTES)


@App.errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"The URL you have added is wrong"}), 404

@App.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message":"The method used is not allowed"}), 405