"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables


class Database:
    """class with database configurtions"""

    def __init__(self):
        if not App.config['TESTING']:
            self.con = psycopg2.connect(host="ec2-23-21-147-71.compute-1.amazonaws.com", user="tczqtmilqwvjnb",
                                        password="9f5d9bdedd64445ff23e4c7b01511693525e6823614c43620eaa1356485b0bbf", dbname="d8qmqu2rair9cl")
            
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
            self.con = psycopg2.connect(host="ec2-23-21-147-71.compute-1.amazonaws.com", user="tczqtmilqwvjnb",
                                        password="9f5d9bdedd64445ff23e4c7b01511693525e6823614c43620eaa1356485b0bbf", dbname="test_db")
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

   
