"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables
from config import TestingConfig, DevelopmentConfig
App.config.from_object(TestingConfig)
import os


class Database:
    """class with database configurtions"""

    def __init__(self):
        
                        
        if not App.config.from_object(TestingConfig):            
            self.con = psycopg2.connect(os.environ('DATABASE_URL'))
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()

        else:
            print("====Tetsts Run===",App.config['TESTING'])
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="moschinogab19", dbname="test_db")
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()