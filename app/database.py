"""Database config file"""
from datetime import date
import psycopg2
from app import App
from app.model import tables
import os
from config import DevelopmentConfig

App.config.from_object(DevelopmentConfig)


class Database:
    """class with database configurtions"""

    def connection(self):
        if App.config.from_object(DevelopmentConfig):
            self.con = psycopg2.connect(
                                        database=App.config['DB_NAME'],
                                        user=App.config['DB_USER'],
                                        password=App.config['DB_PASS'],
                                        host=App.config['DB_HOST'],
                                        port=App.config['DB_PORT'])
            self.con.autocommit = True
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con

        else:            
            self.con =psycopg2.connect(
                                        database=App.config['DB_NAME'],
                                        user=App.config['DB_USER'],
                                        password=App.config['DB_PASS'],
                                        host=App.config['DB_HOST'],
                                        port=App.config['DB_PORT'])
            self.con.autocommit = True
            cur = self.con.cursor()
            cur.execute(tables.USER,)
            cur.execute(tables.FOODITEM,)
            cur.execute(tables.ORDER,)
            self.con.commit()
            return self.con