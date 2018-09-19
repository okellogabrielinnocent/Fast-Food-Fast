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
            "Orderd At": str(datetime.now())
        }
        self.orders.append(order)
        return order
    
    def get_all_orders(self):
        """Return list of all orders
        This function gather all the orders made by user
        """
        return self.orders