"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables
import os
from config import TestingConfig, DevelopmentConfig
App.config.from_object(TestingConfig)


class Database:
    """class with database configurtions"""

    def connection(self):
        if App.config.from_object(TestingConfig)==True:
            self.con = psycopg2.connect('postgres://txulbvjcwlqbtl:9c025a0dae4d90c9f64c3dbb94a83298229cdc6227dffac4525cee38600aa35e@ec2-23-21-171-249.compute-1.amazonaws.com:5432/d1c60svhtc6rcr')
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con

        else:            
            self.con = psycopg2.connect('postgres://txulbvjcwlqbtl:9c025a0dae4d90c9f64c3dbb94a83298229cdc6227dffac4525cee38600aa35e@ec2-23-21-171-249.compute-1.amazonaws.com:5432/d1c60svhtc6rcr')
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con