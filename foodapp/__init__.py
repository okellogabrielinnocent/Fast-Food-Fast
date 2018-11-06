from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# from flasgger import Swagger

app = Flask(__name__, template_folder ='../templates', static_folder='../satic')
app.config['JWT_SECRET_KEY'] = 'innocorp'
jwt = JWTManager(app)
cors = CORS(app, resources={r"/API/*": {"origins": "*"}})
# Swagger(App)
'''JWT MAnager
An object used to hold JWT settings and callback functions
for the Flask-JWT-Extended extension.'''

from foodapp.api.api import ROUTES
app.register_blueprint(ROUTES)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"The URL you have added is wrong {}".format(error)}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message":"The method used is not allowed"}), 405