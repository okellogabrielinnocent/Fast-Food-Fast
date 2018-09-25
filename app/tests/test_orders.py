""" test base page"""
import unittest
import uuid
from app.api.api import app
from flask import json


        
class TestBase(unittest.TestCase):
    app.app_context().push()
    

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
        """Define test variables and initialize app."""
        self.empty_order = {}

        self.make_order = json.dumps(dict(
                    description="Rice and meat",
                    client="Gabriel",
                    location="Kisaasi",
                    quantity=2, 
                    status="Pending"
                    ))
        
                    
        self.get_orders = json.dumps({
                            "Orderd At": "2018-09-20 10:03:53.072350",
                            "client": "Gabriel",
                            "description": 2,
                            "id": str(uuid.uuid4()),
                            "location": "Kisaasi",
                            "quantity": 2,
                            "status": "Pending"
                        })

        self.wrong_id_orders = json.dumps({
                            "Orderd At": "2018-09-20 10:03:53.072350",
                            "client": "Gabriel",
                            "description": 2,
                            "id": "f262b0b6-be59-11e8-9e8b-e24b8e248ee6",
                            "location": "Kisaasi",
                            "quantity": 2,
                            "status": "Pending"
                        })
    
    def test_get_orders(self):
        '''create order'''
        res = self.client.post('/api/v1/orders', 
                                    data=json.dumps(dict(description="Rice and meat",
                                                            client="Gabriel",
                                                            location="Kisaasi",
                                                            quantity=2, 
                                                            status="Pending")), 
                                                            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        '''check whether order with given id is there'''
        response = self.client.get('/api/v1/orders',
                          content_type='application/json', 
                                data=json.dumps(self.get_orders)
                                )
                                
        self.assertIn(b'Orders', response.data)
        self.assertEqual(response.status_code, 200)

    
    def test__get_order_with_wrong_id(self):
        
        response = self.client.get('/api/v1/orders'+ "/f262b0b6-be59-11e8-9e8b-e24b8e248ee6", 
                                data=json.dumps(self.get_orders)
                                )

        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Order not avialable',response.data)

    def test_to_create_order(self):
            """test to create an order"""

            res = self.client.post('/api/v1/orders', 
                                    data=json.dumps(dict(description="Rice and meat",
                                                            client="Gabriel",
                                                            location="Kisaasi",
                                                            quantity=2, 
                                                            status="Pending")), 
                                                            content_type='application/json')
            self.assertEqual(res.status_code, 201)
            self.assertIn(b"Order", res.data)

    def test_to_make_wrong_order(self):
            """test to create an order"""

            res = self.client.post('/api/v1/orders', 
                                    data="Wrong data",                                                      content_type='application/json')
            self.assertEqual(res.status_code, 400)
            self.assertIn(b"Bad Request", res.data)
    
    

if __name__ == '__main__':
    unittest.main()
