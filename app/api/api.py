import json
from flask import Flask, Response, request, jsonify
from app.model.order import Order

app = Flask(__name__)

orders = Order()

@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    if len(orders.get_all_orders())==0:
        response = jsonify({"message":"You have not ordered yet"}) 
        response.status_code = 404
        return response
    if len(orders.get_all_orders())>=1:
        order = orders.get_all_orders()
        response = jsonify({"Orders": order}) 
        response.status_code = 200 
        return response
    
@app.route('/api/v1/orders', methods=['POST'])
def make_order():
    """
    Add new order to order lists.
    """
    data = request.get_json()
    check_order = orders.create_order(data['description'], data['client'], data['location'], data['quantity'])
    if not check_order:
        response =jsonify({"message": "Unable process your order"})
        response.status_code = 200
        return response

    if check_order:
        response= jsonify({"messege": check_order})
        response.status_code = 201
        return response