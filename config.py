class Config():
    DEBUG = False
    SECRET_KEY = "whsdyuhgshji90woiryh3ikwgrdn9w7eui3kgwbnidjhnsmufycneh"
    DB_NAME = "d1c60svhtc6rcr"
    DB_USER = "txulbvjcwlqbtl"
    DB_PASS = "9c025a0dae4d90c9f64c3dbb94a83298229cdc6227dffac4525cee38600aa35e"
    DB_HOST = "ec2-23-21-171-249.compute-1.amazonaws.com"
    


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
   