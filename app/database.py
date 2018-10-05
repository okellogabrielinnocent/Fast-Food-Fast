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
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="test_db")
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con

        else:            
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="fastfoodfast")
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con