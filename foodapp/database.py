"""Database config file"""
from datetime import date
import psycopg2
from foodapp import app
from foodapp.model import tables


class Database:
    """class with database configurtions"""

    def __init__(self):
        if not app.config['TESTING']:
            self.con = psycopg2.connect(host="ec2-107-20-211-10.compute-1.amazonaws.com", user="yiglrgdinuufse",
                                        password="38930676ea20c42391dc9c13c91270f6af8af6c235b2bbb9b7dee05e2041886c", dbname="d2datun196lfag")
            
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
            self.con = psycopg2.connect(host="ec2-107-20-211-10.compute-1.amazonaws.com", user="yiglrgdinuufse",
                                        password="38930676ea20c42391dc9c13c91270f6af8af6c235b2bbb9b7dee05e2041886c", dbname="d2datun196lfag")
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
        con = psycopg2.connect(host="d2datun196lfag", user="yiglrgdinuufse",
                               password="moschinogab19", dbname="test_db")
        return con

    def closedb(self):
        """method to close db connection"""
        self.con.close()

   
