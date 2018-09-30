import json
from flask import Flask, Response, request, jsonify
from app.model.order import Order
import logging

app = Flask(__name__)

orders = Order()

@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """
    Get all orders from order lists.
    """
    order =orders.get_all_orders()
    if len(order)==0:
        return jsonify({"message":"You have not ordered yet"}),400
        
    else: 
        return jsonify({"Orders": order}),200 
    
@app.route('/api/v1/orders', methods=['POST'])
def make_order():
    """
    Add new order to order lists.
    """
    try:
        data = request.get_json()
        
        check_order = orders.create_order(data['description'], 
                                        data['client'],
                                        data['location'],
                                        data['quantity'])
        
    except Exception as err:
        return jsonify({"Message": "Please add the {}  field".format(str(err))}), 400

    if data['description'] is None or type(data['description']) != str or data['description'] is "" :
        return jsonify({"Message":"Description should be charactor"}), 400

    else:
        return jsonify({"Order": check_order}), 201

@app.route('/api/v1/orders/<order_id>',  methods=['GET'])
def get_order(order_id):
    """
    Get order from order lists.
    """
    result = orders.get_order(order_id)
    if not result:
        return jsonify({"message": "Order not avialable"}),404

    else:
        return jsonify({"Your order": result}),200

@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def put_order(order_id):
    """
    Update order to order lists.
    """
    data = request.get_json()
    order_status = data['status']
    
    if order_status not in ['Accepted', 'Rejected']:
        return jsonify({"message":"Bad request. Invalid order status"}), 400
    else:
        return jsonify({"message": orders.put_order(order_id)}), 200

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"The URL you have added is wrong"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message":"The methode used is not allowed"}), 405