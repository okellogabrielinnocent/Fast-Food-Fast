import unittest
import json
import psycopg2
from flask_jwt_extended import create_access_token
from app import App
from app.database import Database

        
class TestBase(unittest.TestCase):
    App.app_context().push()
    
    def setUp(self):
        App.config['TESTING'] = True
        self.client = App.test_client()
        with App.test_request_context():
            self.loggedin_user = dict(user_id=1, username='Gabriel',
                                      password='Gabriel', Admin='False')
            self.access_token = create_access_token(self.loggedin_user)
            self.access_header = {'Authorization': 'Bearer {}'.format(
                self.access_token)}
                
        """Define test variables and initialize App."""
    
    def test_page_not_found(self):
        response = self.client.put('/api/v1/')
        self.assertEqual(response.status_code,404)
        self.assertIn(b'The URL you have added is wrong', response.data)
    
    def test_method_not_allowed(self):
        response = self.client.put('/API/v1/auth/user/signup')
        self.assertEqual(response.status_code,405)
        self.assertIn(b'The method used is not allowed', response.data)
    
    def tearDown(self):
        users= ("""DROP TABLE IF EXISTS users CASCADE;""")
        food_item = ("""DROP TABLE IF EXISTS food_item CASCADE;""")
        order= ("""DROP TABLE IF EXISTS oders CASCADE;""")
        menu = ("""DROP TABLE IF EXISTS menu CASCADE;""")
        
        self.con = psycopg2.connect(host="localhost", user="postgres",
                               password="moschinogab19", dbname="test_db")
        cur = self.con.cursor()
        cur.execute(users,)
        cur.execute(food_item,)
        cur.execute(order,)
        cur.execute(menu,)
        self.con.commit()

if __name__ == '__main__':
    unittest.main()
