from datetime import datetime
import uuid

class Order:
    
    def __init__(self):
        self.orders = []
    
    def get_all_orders(self):
        """Return list of all orders
        This function gather all the orders made by user
        """
        return self.orders