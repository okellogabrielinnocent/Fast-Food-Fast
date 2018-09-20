""" test base page"""
import unittest
from app.api.api import app
from flask import json

class TestBase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        """Define test variables and initialize app."""
        self.empty_order = {}

        self.make_order = json.dumps({
                    "description":"Rice and meat",
                    "client":"Gabriel",
                    "location":"Kisaasi",
                    "quantity":2, 
                    "status":"Pending"
                    })
        self.get_orders = json.dumps({
                            "Orderd At": "2018-09-20 10:03:53.072350",
                            "client": "Gabriel",
                            "description": 2,
                            "id": "553f9cb4-bca3-11e8-a435-8056f2cd6b0b",
                            "location": "Kisaasi",
                            "quantity": 2,
                            "status": "Pending"
                        })
        
    
    def test_no_orders(self):
        
        response = self.client.get('/api/v1/orders', 
                                data=json.dumps(self.empty_order)
                                )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have not ordered yet',response.data)
    
    def test_get_orders(self):

        response = self.client.get('/api/v1/orders', 
                                data=json.dumps(self.get_orders)
                                )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have not ordered yet',response.data)

    def test_make_order(self):
    
        response = self.client.get('/api/v1/orders', 
                                data=json.dumps(self.get_orders)
                                )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have not ordered yet',response.data)
    



if __name__ == '__main__':
    unittest.main()
