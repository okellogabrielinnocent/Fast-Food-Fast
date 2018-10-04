"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables
from config import TestingConfig, DevelopmentConfig
App.config.from_object(TestingConfig)
App.config['DEBUG']

class Database:
    """class with database configurtions"""

    def __init__(self):
        if App.config['TESTING']:
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="fastfoodfast")
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()

        else:
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="test_db")
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur =self.con.commit()
            cur.execute("""INSERT INTO users(username, password, address,
                            email, admin)
            VALUES ('okello','moschinogab','kisaasi','okellogabrielinnocent@gmail.com', 'TRUE')""")
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.FOODITEM,)
            self.con.commit()
            cur.execute("""INSERT INTO food_item(description, price, user_userid)VALUES(1;"Meat and Rice";2000;4)""")
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.ORDER,)
            cur.execute("""INSERT INTO orders(description, price, user_userid)VALUES(1;"Meat and Rice";2000;4)""")
            self.con.commit()