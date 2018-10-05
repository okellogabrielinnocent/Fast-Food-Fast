import os
SECRET_KEY = os.environ.get('DB_PASS')
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'DB_PASS'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    TESTING = True

