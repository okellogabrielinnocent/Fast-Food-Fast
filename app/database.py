# """Database config file"""
# from datetime import date
# import psycopg2
# from app import App
# from app.model import tables
# import os
# from config import DevelopmentConfig

# App.config.from_object(DevelopmentConfig)


# class Database:
#     """class with database configurtions"""

#     def connection(self):
#         if App.config.from_object(DevelopmentConfig):
#             self.con = psycopg2.connect(
#                                         database=App.config['DB_NAME'],
#                                         user=App.config['DB_USER'],
#                                         password=App.config['DB_PASS'],
#                                         host=App.config['DB_HOST'],
#                                         port=App.config['DB_PORT'])
#             self.con.autocommit = True
#             cur = self.con.cursor()
#             cur.execute(tables.USER,)
#             self.con.commit()
#             cur = self.con.cursor()
#             cur.execute(tables.FOODITEM,)
#             self.con.commit()
#             cur = self.con.cursor()
#             cur.execute(tables.ORDER,)
#             self.con.commit()
#             return self.con

#         else:            
#             self.con =psycopg2.connect(
#                                         database=App.config['DB_NAME'],
#                                         user=App.config['DB_USER'],
#                                         password=App.config['DB_PASS'],
#                                         host=App.config['DB_HOST'],
#                                         port=App.config['DB_PORT'])
#             self.con.autocommit = True
#             cur = self.con.cursor()
#             cur.execute(tables.USER,)
#             cur.execute(tables.FOODITEM,)
#             cur.execute(tables.ORDER,)
#             self.con.commit()
#             return self.con
"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables

# D = Database()
class Database:
    """class with database configurtions"""

    def __init__(self):
        if not App.config['TESTING']:
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="fastfoodfast")
            
            self.con.autocommit = True
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.FOODITEM,)
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.ORDER,)
            self.con.commit()
        else:
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="test_db")
            self.con.autocommit = True
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.FOODITEM,)
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.ORDER,)
            self.con.commit()

    @classmethod
    def testing_db_teardown(cls):
        """method to delete tables after testing"""
        con = psycopg2.connect(host="localhost", user="postgres",
                               password="moschinogab19", dbname="test_db")
        return con

    def closedb(self):
        """method to close db connection"""
        self.con.close()

   
