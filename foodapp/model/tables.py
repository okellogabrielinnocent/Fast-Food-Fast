"""SQL TABLES"""
# -- -----------------------------------------------------
# -- Table users
# -- -----------------------------------------------------
# DROP TABLE IF EXISTS food_item ;

USER = """CREATE TABLE IF NOT EXISTS users (
  userid SERIAL NOT NULL,
  username VARCHAR(45) NULL,
  password VARCHAR(45) NULL,
  address VARCHAR(45) NULL,
  email VARCHAR(45) NULL,
  admin BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (userid))"""


# -- -----------------------------------------------------
# -- Table food_item
# -- -----------------------------------------------------
# DROP TABLE IF EXISTS food_item ;

FOODITEM = """CREATE TABLE IF NOT EXISTS food_item (
  itemid SERIAL NOT NULL,
  description VARCHAR(45) NULL,
  price INT NULL,
  user_userid INT NOT NULL,
  PRIMARY KEY (itemid),
  CONSTRAINT fk_food_item_user1
    FOREIGN KEY (user_userid)
    REFERENCES users (userid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)"""
# -- -----------------------------------------------------
# -- Table order
# -- -----------------------------------------------------
# DROP TABLE IF EXISTS order ;

ORDER = """CREATE TABLE IF NOT EXISTS orders (
  orderid SERIAL NOT NULL,
  order_status VARCHAR(25) NOT NULL DEFAULT 'NEW',
  order_date VARCHAR(45) NULL,
  user_userid INT NOT NULL,
  food_item_itemid INT NOT NULL,
  quantity INT NULL,
  PRIMARY KEY (orderid),
  CONSTRAINT fk_order_user1
    FOREIGN KEY (user_userid)
    REFERENCES users (userid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_order_food_item1
    FOREIGN KEY (food_item_itemid)
    REFERENCES food_item (itemid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)"""