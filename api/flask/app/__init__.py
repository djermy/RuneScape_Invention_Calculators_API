# system
import logging, os
from dotenv import load_dotenv

# flask
from apiflask import APIFlask
from flask_cors import CORS, cross_origin
import app.config as config 

# store
from app.database.store import get_store

# init
load_dotenv()

# define create app function to make instance of app
def create_app():

    # init app
    app = APIFlask(__name__)
    match os.getenv('ENVIRONMENT'):
        case 'production':
            app.config.from_object(config.ProductionConfig)
            print(1)
        case 'development':
            app.config.from_object(config.DevelopmentConfig)
            print(2)
        case 'testing':
            app.config.from_object(config.TestingConfig)
            print(3)
        case _:
            app.config.from_object(config.Config)
            print(4)
    cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    print(f'Listening on http://0.0.0.0:5000', flush=True)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Content-Type', 'application/json')
        return response

    with app.app_context():

        # create database
        get_store()
        from . import endpoints
    
    return app