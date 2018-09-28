from flask import jsonify, request
from datetime import datetime
class Order:
    
    def __init__(self):
        self.orders = []
        
    def create_order(self, description, client, location, quantity):
        """Make a New order
        This function uses the following param: description, client, location, quantity
        The id is passed in as an auto increment id

        """
        
        data = request.get_json()
        number_of_orders = 1
        for i in range(len(self.orders)):
            number_of_orders += 1
        data['id'] = number_of_orders
        order = {
            "id":str(number_of_orders),
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
        This function gathers all the orders made by user
        """
        return self.orders

    
    def get_order(self, order_id):
        """Return order with specific id
        This function gets order for specfied id on the url
        """
        response = [order for order in self.orders if order['id'] == order_id]
        return response

    def put_order(self, order_id):
        """
         method to update specific order based on the id.
        """
        data = request.get_json()
        order_data = [ order for order in self.orders if (order['id'] == order_id) ]
        order_data[0]['status'] = data['status']
        order_data[0]['description'] = data['description']
        order_data[0]['client'] = data['client']
        order_data[0]['location'] = data['location']
        order_data[0]['quantity'] = data['quantity']
        return order_data