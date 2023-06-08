from service.calculators.alchemiser import alchemiser_calculator
from service.calculators.disassembler import disassembler_calculator
import constants
from flask import Flask
import sys, json

app = Flask(__name__)

@app.route('/items')
def items():
    pass

@app.route('/disassembler/options')
def disassembler_options():
    json = []

    for idx, item in enumerate(constants.ITEMS):
        option = {}
        option['id'] = idx
        option['item'] = item
        json.append(option)

    return str(json)

@app.route('/alchemiser/<int:id>')
def alchemiser(id):
    pass

@app.route('disassembler/options/<int:option_index>')
def disassembler(option_index):
    pass

'''
def main():
    #alchemiser_calculator()
    disassembler_calculator()
    return 0

if __name__ == '__main__':
    sys.exit(main())
'''