"""Database config file"""
from datetime import date
import psycopg2
from foodapp import App
from foodapp.model import tables


class Database:
    """class with database configurtions"""

    def __init__(self):
        if not App.config['TESTING']:
            self.con = psycopg2.connect(host="ec2-23-21-171-249.compute-1.amazonaws.com", user="txulbvjcwlqbtl",
                                        password="9c025a0dae4d90c9f64c3dbb94a83298229cdc6227dffac4525cee38600aa35e", dbname="d1c60svhtc6rcr")
            
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
            self.con = psycopg2.connect(host="ec2-23-21-171-249.compute-1.amazonaws.com", user="txulbvjcwlqbtl",
                                        password="9c025a0dae4d90c9f64c3dbb94a83298229cdc6227dffac4525cee38600aa35e", dbname="test_db")
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

   
