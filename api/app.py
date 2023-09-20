# system
import os, json, dotenv, logging, api.constants

# flask
from flask import Flask
from flask_cors import CORS, cross_origin

# calculators
from api.service.calculators.alchemiser import alchemiser_calculator
from api.service.calculators.disassembler import disassembler_calculator
from api.service.calculators.plank_maker import plank_calculator

# store
from api.database.store import store
from api.service.runescape.items import get_all_items

# init
dotenv.load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# create database
store.create_database()

print(f'Listening on http://0.0.0.0:5000', flush=True)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def health():
    return json.dumps({'message': 'Welcome to the RuneScape Calculator API'})

@app.route('/items')
def items():
    return json.dumps(runescape_item.get_all())

@app.route('/disassembler/options')
def disassembler_options():
    choices = []

    for idx, item in enumerate(api.constants.ITEMS):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return json.dumps(choices)

@app.route('/alchemiser/<int:item_id>')
def alchemiser(item_id):
    return json.dumps(alchemiser_calculator(item_id))

@app.route('/disassembler/<int:option_idx>')
def disassembler(option_idx):
    return json.dumps(disassembler_calculator(option_idx))

@app.route('/plank_maker/options')
def plank_maker_options():
    choices = []

    for idx, item in enumerate(api.constants.PLANK_MAKER_INPUT):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return json.dumps(choices)

@app.route('/plank_maker/<int:option_idx>')
def plank_maker(option_idx):
    return json.dumps(plank_calculator(option_idx))

@app.route('/update_database/<int:secret_key>')
def update_database(secret_key):
    '''
    !DANGEROUS!
    Updates the database..
    Requires secret key.
    '''

    if secret_key == int(os.getenv('DATABASE_REMAKE_KEY')):
        get_all_items()
        return 'Database successfully updated!'
