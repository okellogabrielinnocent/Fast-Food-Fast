import json
from flask import Flask, Response, request, jsonify
from app.model.order import Order

app = Flask(__name__)

orders = Order()

@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    order =orders.get_all_orders()
    if len(order)==0:
        return jsonify({"message":"You have not ordered yet"}),404
        
    else: 
        return jsonify({"Orders": order}),200 
    
@app.route('/api/v1/orders', methods=['POST'])
def make_order():
    """
    Add new order to order lists.
    """
    try:
        data = request.get_json()

        check_order = orders.create_order(data['description'], data['client'], data['location'],data['price'], data['quantity'])
        
    except Exception as err:
        return jsonify({"Message": "The {} parameter does not exist".format(str(err))}), 400

    else:
        return jsonify({"Order": check_order}), 201

@app.route('/api/v1/orders/<order_id>',  methods=['GET'])
def get_order(order_id):
    result = orders.get_order(order_id)
    if not result:
        return jsonify({"message": "Order not avialable"}),404

    else:
        return jsonify({"Your order": result}),200

@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def put_order(order_id):
    
    data = request.get_json()
    order_status = data['status']
    
    if order_status not in ['Accepted', 'Rejected']:
        
        return jsonify({"message":"Bad request. Invalid order status"}), 400
    elif  not 'description' and 'status'  in data:
        error = 'Please enter correct information'
        return error
    else:
        return jsonify({"message": orders.put_order(order_id)}), 200
    

    