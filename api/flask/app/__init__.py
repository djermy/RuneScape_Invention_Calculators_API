# system
import logging

# flask
from flask import Flask
from flask_cors import CORS, cross_origin
from app.config import Config 

# store
from app.database.store import store

# init
app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# create database
store.create_database()

print(f'Listening on http://0.0.0.0:5000', flush=True)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

from app import endpoints