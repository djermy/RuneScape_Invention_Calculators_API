import os
from dotenv import load_dotenv

load_dotenv()

# flask config
class Config:
    SECRET_KEY = os.getenv('RS_CALCULATOR_API_KEY')
    DEBUG = False