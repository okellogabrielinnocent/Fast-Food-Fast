""" test base page"""
import unittest
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
                            "id": "553f9cb4-bca3-11e8-a435-8056f2cd6b0b",
                            "location": "Kisaasi",
                            "quantity": 2,
                            "status": "Pending"
                        })

        self.wrong_id_orders = json.dumps({
                            "Orderd At": "2018-09-20 10:03:53.072350",
                            "client": "Gabriel",
                            "description": 2,
                            "id": "a435-8056f2cd6b0b",
                            "location": "Kisaasi",
                            "quantity": 2,
                            "status": "Pending"
                        })
        
    
    def test_no_orders(self):
        
        response = self.client.get('/api/v1/orders',
                                content_type='application/json', 
                                data=json.dumps(self.empty_order)
                                )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have not ordered yet',response.data)
    
    # def test_get_orders(self):

    #     response = self.client.get('/api/v1/orders',
    #                       content_type='application/json', 
    #                             data=json.dumps(self.get_orders)
    #                             )
                                
    #     self.assertIn(b'Orders', response.data)
    #     self.assertEqual(response.status_code, 200)

    
    def test__get_order_with_wrong_id(self):
        
        response = self.client.get('/api/v1/orders/553f9cb4-bca3-11e8-a435-8056f2cd6b0b', 
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
    
    # def test_put_order(self):
    #     response = self.client.put('/api/v1/orders/5b1f7f70-bd6f-11e8-9968-8056f2cd6b0b',
    #                                 content_type ='application/json',
    #                                 data = json.dumps({"status": "Accepted" } )
    #                                 )
    #     self.assertEqual(response.status_code,201)




if __name__ == '__main__':
    unittest.main()
