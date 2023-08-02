from api.service.calculators.alchemiser import alchemiser_calculator
from api.service.calculators.disassembler import disassembler_calculator
from api.service.calculators.plank_maker import plank_calculator
from api.database.database_handler import grab_all_items
from flask import Flask
import os, json, dotenv, api.constants

dotenv.load_dotenv()
app = Flask(__name__)

# VALIDATED
@app.route('/items')
def items():
    return json.dumps(grab_all_items())

# VALIDATED
@app.route('/disassembler/options')
def disassembler_options():
    choices = []

    for idx, item in enumerate(api.constants.ITEMS):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return json.dumps(choices)

# VALIDATED
@app.route('/alchemiser/<int:item_id>')
def alchemiser(item_id):
    return json.dumps(alchemiser_calculator(item_id))

# VALIDATED
@app.route('/disassembler/<int:option_idx>')
def disassembler(option_idx):
    return json.dumps(disassembler_calculator(option_idx))

# VALIDATED
@app.route('/plank_maker/options')
def plank_maker_options():
    choices = []

    for idx, item in enumerate(api.constants.PLANK_MAKER_INPUT):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return json.dumps(choices)

# VALIDATED
@app.route('/plank_maker/<int:option_idx>')
def plank_maker(option_idx):
    return json.dumps(plank_calculator(option_idx))

@app.route('/remake_database/<int:secret_key>')
def remake_database(secret_key):
    if secret_key == int(os.getenv('DATABASE_REMAKE_KEY')):
        return