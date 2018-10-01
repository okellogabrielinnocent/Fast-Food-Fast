import unittest
import json
from flask_jwt_extended import create_access_token
from app import App
from app.database import Database

        
class TestBase(unittest.TestCase):
    App.app_context().push()
    
    def setUp(self):
        App.testing = True
        self.client = App.test_client()
        
        """Define test variables and initialize App."""
    
    def test_page_not_found(self):
        response = self.client.put('/api/v1/')
        self.assertIn(b'The URL you have added is wrong', response.data)
    
    def test_method_not_allowed(self):
        response = self.client.put('/api/v1/orders')
        self.assertIn(b'The URL you have added is wrong', response.data)

if __name__ == '__main__':
    unittest.main()
