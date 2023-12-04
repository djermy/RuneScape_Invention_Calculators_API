import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    TESTING = False
    SECRET_KEY = os.getenv('RS_CALCULATOR_API_KEY')
    DEBUG = False

class ProductionConfig(Config):
    DB_PATH = 'app/database/rs_items.db'

class DevelopmentConfig(Config):
    DB_PATH = 'app/database/rs_items.db'

class TestingConfig(Config):
    TESTING = True
    DB_PATH = 'app/database/test.db'