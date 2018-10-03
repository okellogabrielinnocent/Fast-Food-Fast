import re
class Validations():
    """validation class with regular expressions"""
    
    """valiation class for order inputs"""
    def __init__(self, description, client,price, quantity):
        self.description = description
        self.client = client
        self.price = price
        self.quantity = quantity
    
    
    def validate_empty(self):
        """method to validate my input """
        
        empty = re.search("^{\\s|\\S}*{\\S}+{\\s|\\S}*$", self.description)
        if not empty:
            return False
        elif not re.search("[a-zA-Z]", self.description):
            return False
        else:
            return True

    @classmethod
    def validate_order_fields(cls, data):
        """method to update other data fields"""
        if not re.search("[a-zA-Z]", data):
            return False

    @classmethod
    def validate_price(cls, data):
        """method to validate as digits"""
        if not re.search("[0-9]", data):
                return False