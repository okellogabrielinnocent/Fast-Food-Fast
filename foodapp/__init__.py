from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# from flasgger import Swagger

App = Flask(__name__)
App.config['JWT_SECRET_KEY'] = 'innocorp'
jwt = JWTManager(App)
cors = CORS(App, resources={r"/API/*": {"origins": "*"}})
# Swagger(App)
'''JWT MAnager
An object used to hold JWT settings and callback functions
for the Flask-JWT-Extended extension.'''

from foodapp.api.api import ROUTES
App.register_blueprint(ROUTES)


@ROUTES.errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"The URL you have added is wrong"}), 404

@ROUTES.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message":"The method used is not allowed"}), 405