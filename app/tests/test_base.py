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
    create_user = json.dumps(dict(username="Cent", admin="False",
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
    
    login_wrong_credentials = (dict(username="okello", password="Gabriel"))

    """Test cases for creating food items and orders"""
    create_food_item = json.dumps(dict(description="Innovet mashed source",
	                            price=2000, user_id =1 ))
    
    create_duplicate_food_item = json.dumps(dict(description="Casava mashed source",
	                            price=2000, user_id =1 ))
    create_food_item_with_empty_data = json.dumps(dict(description=" ",
	                            price=2000, user_id =1 ))
    create_food_item_with_missing_field = json.dumps(dict(price=2000, user_id =1 ))
    get_food_items = json.dumps(dict())
    place_order = json.dumps(dict(food_item_itemid=1,quantity=4))
    place_order_with_no_itemid = json.dumps(dict())

    get_order_by_id = json.dumps(dict(orderid=7,order_status="NEW",
                                    order_date="2018-10-04 20:42:57.780776",
                                    user_userid=1,food_item_itemid=1,quantity=4))
    update_order = json.dumps(dict(orderid=7,order_status="Cancelled"))
    update_order_with_wrong_id = json.dumps(dict(orderid=5,order_status="Pending"))
    update_order_with_no_fields = json.dumps(dict())


    def setUp(self):
        self.client = App.test_client()
        with App.test_request_context():
            self.loggedin_user1 = dict(user_id=1, username='Gabriel',
                                      password='Gabriel', Admin='False')
            self.access_token = create_access_token(self.loggedin_user1)
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
