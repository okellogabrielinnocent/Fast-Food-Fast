class Config():
    DEBUG = False
    DB_NAME = "d8qmqu2rair9cl"
    DB_USER = "tczqtmilqwvjnb"
    DB_PASS = "9f5d9bdedd64445ff23e4c7b01511693525e6823614c43620eaa1356485b0bbf"
    DB_HOST = "ec2-23-21-147-71.compute-1.amazonaws.com"
    


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "fastfoodfast"
    DB_USER = "postgres"
    DB_PASS = "moschinogab19"
    DB_HOST = "localhost"
    


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = "test_db"
    DB_USER = "postgres"
    DB_PASS = "moschinogab19"
    DB_HOST = "localhost"
   