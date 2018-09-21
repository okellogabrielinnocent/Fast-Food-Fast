from flask import jsonify, request
from datetime import datetime
import uuid

class Order:
    
    def __init__(self):
        self.orders = []
        
    def create_order(self, description, client, location, quantity):
        """Make a New order
        This function uses the following param: description, client, location, quantity
        The id is passed in as uuid
        UUID objects (universally unique identifiers) according to RFC 4122.

        """
        order = {
            "id": str(uuid.uuid1()),
            "description": description,
            "client": client,
            "location": location,
            "quantity": quantity,
            "status": "Pending",
            "Orderd_At": str(datetime.now())
        }
        self.orders.append(order)
        return order
    
    def get_all_orders(self):
        """Return list of all orders
        This function gather all the orders made by user
        """
        return self.orders

    
    def get_order(self, order_id):
        response = [order for order in self.orders if order['id'] == order_id]
        return response

    def put_order(self, order_id):
        """
         method to update specific order based on the id.
        """
        data = request.get_json()
        order_data = [ order for order in self.orders if (order['id'] == order_id) ]
        order_data[0]['status'] = data['status']

        
        if 'client' in data : 
            order_data[0]['client'] = data['client']
        return order_data