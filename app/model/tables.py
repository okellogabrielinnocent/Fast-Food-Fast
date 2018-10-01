"""SQL TABLES"""


USER = """CREATE TABLE IF NOT EXISTS users (
  userid SERIAL NOT NULL,
  username VARCHAR(45) NULL,
  password VARCHAR(45) NULL,
  address VARCHAR(45) NULL,
  email VARCHAR(45) NULL,
  admin BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (userid))"""


# FOODITEM = """CREATE TABLE IF NOT EXISTS food_item (
#   itemid SERIAL NOT NULL,
#   description VARCHAR(45) NULL,
#   price INT NULL,
#   user_userid INT NOT NULL,
#   PRIMARY KEY (itemid),
#   CONSTRAINT fk_food_item_user1
#     FOREIGN KEY (user_userid)
#     REFERENCES user (userid)
#     ON DELETE NO ACTION
#     ON UPDATE NO ACTION)"""


MENU ="""CREATE TABLE IF NOT EXISTS menu (
  menuid SERIAL NOT NULL,
  meal VARCHAR(45) NULL,
  food_item_itemid SERIAL NOT NULL,
  PRIMARY KEY (menuid),
  CONSTRAINT fk_menu_food_item1
    FOREIGN KEY (food_item_itemid)
    REFERENCES food_item (itemid))"""



ORDER = """CREATE TABLE IF NOT EXISTS order (
  orderid SERIAL NOT NULL,
  status ENUM('Accepted', 'Rejected', 'Pending') NULL,
  date DATETIME NULL,
  menu_menuid INT NOT NULL,
  user_userid INT NOT NULL,
  PRIMARY KEY (orderid),
  INDEX fk_order_menu_idx (menu_menuid ASC),
  INDEX fk_order_user1_idx (user_userid ASC),
  CONSTRAINT fk_order_menu
    FOREIGN KEY (menu_menuid)
    REFERENCES menu (menuid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_order_user1
    FOREIGN KEY (user_userid)
    REFERENCES user (userid))"""
