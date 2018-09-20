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