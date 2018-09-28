"""validation class with regular expressions"""
import re

class Validate():
    """valiation class for order inputs"""
    def __init__(self, description, client,location, quantity):
        self.title = description
        self.client = client
        self.location = location
        self.quantity = quantity

    @classmethod
    def validate_order_fields(cls, decription):
        """method to update other data fields"""
        result = ""
        lst = list(decription)
        for char in lst:
            if not re.search("[a-zA-Z]", char):
                result = False
                break
            else:
                result = True
        return result

    @classmethod
    def validate_price_and_quantity(cls, data):
        """method to validate as digits"""
        result = ""
        lst = list(data)
        for char in lst:
            if not re.search("[0-9]", char):
                result = False
                break    
            else:
                result = True
        return result