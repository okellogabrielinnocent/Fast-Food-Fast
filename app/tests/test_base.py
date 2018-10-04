import unittest
import json
from flask_jwt_extended import create_access_token
from app import App
import psycopg2
from app.database import Database


class TestBase(unittest.TestCase):
    App.app_context().push()
    """class containing test cases for testing """

    """Test cases for user registration and user login"""
    create_user = json.dumps(dict(username="innocent", admin="False",
                                password="Gabriel",address="Kisaasi",
                                email="okellogabrielinnocent@gmail.com"))
    duplicate_user = json.dumps(dict(username="innocent", admin="False",
                                password="Gabriel",address="Kisaasi",
                                email="okellogabrielinnocent@gmail.com"))
    empty_username = json.dumps(dict(username="", admin="False",
                                password="Gabriel",address="Kisaasi",
                                email="okellogabrielinnocent@gmail.com"))
    validate_number_in_field = json.dumps(dict(username="123344", admin="False",
                                password="Gabriel",address="Kisaasi",
                                email="okellogabrielinnocent@gmail.com"))
    missing_username_field = json.dumps(dict(admin="False",
                                password="Gabriel",address="Kisaasi",
                                email="okellogabrielinnocent@gmail.com"))                                    
    user_login = json.dumps(dict(username="Gabriel", password="Gabriel"))
    missing_login_fields = json.dumps(dict())
    login_wrong_credentials = (dict(username="okello", password="Gabriel"))

    def setUp(self):
        App.config['TESTING'] = True
        self.client = App.test_client()
        with App.test_request_context():
            self.loggedin_user = dict(userid=1, username='Gabriel',
                                      password='Gabriel', Admin='False')
            self.access_token = create_access_token(self.loggedin_user)
            self.access_header = {'Authorization': 'Bearer {}'.format(
                self.access_token)}

    def tearDown(self):
        users= ("""DROP TABLE IF EXISTS users CASCADE;""")
        food_item = ("""DROP TABLE IF EXISTS food_item CASCADE;""")
        order= ("""DROP TABLE IF EXISTS oders CASCADE;""")
        
        self.con = psycopg2.connect(host="localhost", user="postgres",
                               password="moschinogab19", dbname="test_db")
        cur = self.con.cursor()
        cur.execute(users,)
        cur.execute(food_item,)
        cur.execute(order,)
        self.con.commit()
        self.con.close()

if __name__ == '__main__':
    unittest.main()
