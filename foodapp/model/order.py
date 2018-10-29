from datetime import date, datetime
from flask import jsonify
from foodapp.database import Database
connect = Database()

class Orders(Database):
    """Initialize order attributes"""

    def __init__(self):
        # self.con = connect.connection()
        """initializing constructor by 
        calling user class Database
        """
        Database.__init__(self)

    def create_item(self, description, price, user_userid):
        '''Method for creating items and adding them to menu by Admin'''
        cur = self.con.cursor()
        cur.execute("""INSERT INTO food_item(description, price, user_userid)
                    VALUES (%s, %s, %s)""",
                    (description, price, user_userid))
        self.con.commit()
        

    def get_menu_list(self):
        
        """Method for getting items in menu"""
        
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM food_item""")
        result = cur.fetchall()

        menu_list = []
        for menu in result:
            menu_info = {}
            menu_info['itemid'] = menu[0]
            menu_info['description'] = menu[1]
            menu_info['price'] = menu[2]

            menu_list.append(menu_info)
        return menu_list

    def validate_item_creation(self,description, price, user_userid):
            '''Method for validation item creation by Admin'''
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

    def create_order(self, order_date, user_userid, food_item_itemid, quantity):
        '''Method for creating order by admin'''

        cur = self.con.cursor()
        cur.execute("""INSERT INTO orders(order_date, user_userid,food_item_itemid,quantity)
                    VALUES (%s, %s, %s, %s)""",
                    (order_date,user_userid,food_item_itemid,quantity))
        self.con.commit()

    def check_placing_order(self):
        
        """Method for getting itemid in menu
        This method helps check whether item is in menu
        """
        
        cur = self.con.cursor()
        cur.execute("""SELECT itemid FROM food_item""")
        self.con.commit()
        result = cur.rowcount
        if result > 0:
            return True
        else:
            False

    def get_item_info(self, itemid):
        """ Gets the info of the item with the itemid provided"""

        sql = "SELECT description, price " \
              "FROM food_item WHERE itemid=%s" % itemid
        cur = self.con.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        item = {}  # holds item information
        for item_info in result:
            item['description'] = item_info[0]
            item['price'] = item_info[1]
        return item

    
    
    def get_order_list(self):
        
        """Method for checking whether order is avialable"""
        
        cur = self.con.cursor()
        cur.execute("""SELECT * FROM orders""")
        result = cur.fetchall()

        order_list = []
        
        for order in result:
            order_info = {}
            itemid = order[4]            
            item_info = self.get_item_info(itemid)
            order_info['orderid'] = order[0]
            order_info['order_status'] = order[1]
            order_info['order_date'] = order[2]
            order_info['user_userid'] = order[3]
            # order_info['food_item_itemid'] = order[4]
            order_info['quantity'] = order[5]
            order_info['description'] = item_info["description"]
            order_info['price'] = item_info["price"]
            order_list.append(order_info)
        return order_list
        
        
    def order_details(self, orderid):
        """ 
        Returns the details of a order whose id is provided
        """
        cur = self.con.cursor()
        cur.execute("SELECT orderid, order_date, quantity,order_status," \
                    "user_userid FROM orders WHERE orderid =%s" % orderid)
        result = cur.fetchall()
    
        order_list = []
        for info in result:
            order_info = {}
            order_info['orderid'] = info[0]
            order_info['order_date'] = info[1]
            order_info['quantity'] = info[2]
            order_info['order_status'] = info[3]
            order_list.append(order_info)
        return order_list

    def update_order(self, orderid, order_status):
        
            orders_list=[]
            cur = self.con.cursor()
            cur.execute('''UPDATE orders SET order_status = %s WHERE orderid = %s 
                            RETURNING orderid, order_status, order_date, quantity,
                            food_item_itemid, user_userid''', (order_status, orderid))
            updated = cur.fetchone()
            u_ord = {}
            u_ord['orderid'] = updated[0]
            u_ord['order_date'] = updated[2]
            u_ord['quantity'] = updated[5]
            u_ord['order_status'] = updated[1]
            u_ord['food_item_itemid'] = updated[4]
            u_ord['user_userid'] = updated[3]

            orders_list.append(u_ord)
            return orders_list
    