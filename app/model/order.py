from datetime import date, datetime
from flask import jsonify
from app.database import Database


class Orders(Database):
    """Initialize order attributes"""

    def __init__(self):
        """initializing constructor"""
        Database.__init__(self)

    def create_order(self, date,menu_menuid, user_userid ):

        cur = self.con.cursor()
        cur.execute("""INSERT INTO users(date, menu_menuid, user_userid)
                    VALUES (%s, %s, %s, False)""",
                    (date, menu_menuid, user_userid))
        self.con.commit()
    
    def get_order_list(self):
        
        """Method for checking whether order is avialable"""
        
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM orders""")
        result = cur.fetchall()

        order_list = []
        for order in result:
            order_info = {}
            order_info['orderid'] = order[0]
            order_info['date'] = order[1]
            order_info['menu_menuid'] = order[2]
            order_info['user_userid'] = order[4]

            order_list.append(order_info)
        return order_list

        
    def check_if_order_exist(self,orderid, date,menu_menuid, user_userid ):
    
        """Method for checking whether order is avialable"""
        
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM orders where
                    orderid = %s,date = %s, menu_menuid = %s,user_userid = %s""", 
                    (orderid, date, menu_menuid, user_userid ))
        self.con.commit()
        result = cur.rowcount
        if result > 0:
                return True
        else:
            False

    def create_item(self, description, price, user_userid):
        
        cur = self.con.cursor()
        cur.execute("""INSERT INTO food_item(description, price, user_userid)
                    VALUES (%s, %s, %s)""",
                    (description, price, user_userid))
        self.con.commit()

    def get_menu_list(self):
        
        """Method for checking whether order is avialable"""
        
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM menu where price = price""")
        result = cur.fetchall()

        menu_list = []
        for menu in result:
            menu_info = {}
            menu_info['menuid'] = menu[0]
            menu_info['meal'] = menu[1]
            menu_info['price'] = menu[2]

            menu_list.append(menu_info)
        return menu_list

    def validate_item_creation(self,description, price, user_userid):
            
            cur = self.con.cursor()
            cur.execute("""SELECT * FROM food_item where
                        description = %s AND price = %s AND user_userid = %s""", 
                        (description, price, user_userid))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                return True
            else:
                False
