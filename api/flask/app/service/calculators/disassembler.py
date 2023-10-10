import app.service.calculators.calculator_utils as utils
from app.service.runescape.items import get_item_cost
from app.database.store import store
import app.constants

def disassembler_calculator(option_idx):
    '''
    Takes user selection and calculates singular, hourly and daily profit-
    for selected item.
    '''

    choice = option_idx
    profit = calculate_profit(choice)
    return profit

def calculate_profit(item_idx):
    '''
    Calculate and return profits for disassembler calculator.
    '''

    # define chosen items name via index
    item_name = app.constants.ITEMS[item_idx]

    # get item id
    item_id = store.item_store.get_by_name(item_name)['id']

    # get current item cost
    item_cost = get_item_cost(item_id)

    # calculate cost of machine fuel to process 1 item
    cost_of_charges = app.constants.DISASSEMBLER_CHARGES_PER_ITEM * utils.cost_of_charge()

    # total cost to process 1 of the chosen item
    cost_per_item = item_cost + cost_of_charges

    # hourly and daily costs to process chosen item
    hourly = (cost_per_item * app.constants.ITEMS_DISASSEMBLED_PER_HOUR)
    daily = hourly * 24

    # get value of 1 empty divine charge
    empty_divine_charge_value = get_item_cost(app.constants.EMPTY_DIVINE_CHARGE_ID)

    if item_name == 'Soapstone':
        results = utils.soapstone_calculator(daily, empty_divine_charge_value)
        return results
    else:
        results = utils.logs_calculator(item_name, daily, empty_divine_charge_value)
        return results