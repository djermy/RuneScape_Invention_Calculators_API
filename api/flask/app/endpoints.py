import os, json, dotenv
from flask import current_app as app, jsonify

# calculators
from app.service.calculators.alchemiser import alchemiser_calculator
from app.service.calculators.disassembler import disassembler_calculator
from app.service.calculators.plank_maker import plank_calculator
from app.service.calculators.potion_maker import potion_calculator

# store
from app.database.store import get_store
from app.service.runescape.items import get_all_items

# init
dotenv.load_dotenv()
store = get_store()

@app.route('/')
def health():
    return jsonify({'message': 'Welcome to the RuneScape Calculator API'})

@app.route('/items')
def items():
    return jsonify(store.item_store.get_all())

@app.route('/disassembler/options')
def disassembler_options():
    choices = []

    for idx, item in enumerate(constants.ITEMS):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return jsonify(choices)

@app.route('/alchemiser/<int:item_id>')
def alchemiser(item_id):
    return jsonify(alchemiser_calculator(item_id))

@app.route('/disassembler/<int:option_idx>')
def disassembler(option_idx):
    return jsonify(disassembler_calculator(option_idx))

@app.route('/plank_maker/options')
def plank_maker_options():
    choices = []

    for idx, item in enumerate(constants.PLANK_MAKER_INPUT):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return jsonify(choices)

@app.route('/plank_maker/<int:option_idx>')
def plank_maker(option_idx):
    return jsonify(plank_calculator(option_idx))

@app.route('/potion_maker/options')
def potion_maker_options():
    choices = []

    for idx, item in enumerate(constants.POTION_MAKER_HERBS):
        option = {}
        option['id'] = idx
        option['item'] = item
        choices.append(option)

    return jsonify(choices)

@app.route('/potion_maker/<int:option_idx>')
def potion_maker(option_idx):
    return jsonify(potion_calculator(option_idx))