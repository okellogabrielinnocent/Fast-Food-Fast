""" test base page"""
import unittest
from app.api.api import app
from flask import json



class TestBase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_no_orders(self):
        
        response = self.app.get('/api/v1/orders', 
                                data=json.dumps({}),
                                content_type='application/json'
                                )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have not ordered yet', response.data)
    
    
    
if __name__ == '__main__':
    unittest.main()
