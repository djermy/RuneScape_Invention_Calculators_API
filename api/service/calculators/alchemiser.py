from service.runescape.items import get_item_cost
from service.runescape.alchemy import scrape_alch_value
from utils.user_input import get_user_input
from database.database_handler import id_grabber, name_grabber
from service.calculators.calculator_utils import cost_of_charge
import constants

def calculate_profit(item_name, item_id):

    item_cost = get_item_cost(item_id)
    alch_value = get_alch_value(item_name)
    cost_per_item = calculate_fuel_cost()

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = round(alch_value - total_cost_per_item, 2)
    hourly = round((alch_value - total_cost_per_item) * constants.ITEMS_ALCHEMISED_PER_HOUR, 2)
    daily = round(hourly * 24, 2)

    return {
        'profit_or_loss': profit_or_loss,
        'hourly': hourly,
        'daily': daily
    }

# main function
def alchemiser_calculator(item_id):
    '''
    Calculates profit/loss to alchemise the chosen item,
    and returns json output.. 
    '''

    item_name = name_grabber(item_id)
    profit = calculate_profit(item_name, item_id)

    json = [{key:value} for key, value in profit.items()]
    return str(json)

# helper functions
def get_item_id(item_name):
    '''
    Take item_name and returns item_id.
    '''

    item_id = id_grabber(item_name)
    if item_id == None:
        print('Error item not found!')
        print('Perhaps you mispelled it?')
        return alchemiser_calculator()
    
    return item_id

def get_alch_value(item_name):
    '''
    Takes item_name and returns alch_value.
    '''
    
    alch_value = scrape_alch_value(item_name)

    # check alch_value was properly obtained
    if type(alch_value) == str:
        print(alch_value)
        print('Please try again')
        return alchemiser_calculator()

    return alch_value

def calculate_fuel_cost():
    '''
    Calculates and returns cost of machine fuels for 1 item.
    '''

    cost_of_charges = constants.ALCHEMISER_CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = get_item_cost(constants.NATURE_RUNE_ID)
    cost_per_item = round(cost_of_charges + cost_of_nature_rune, 2)

    return cost_per_item

def print_result(results):
    # render output
    print(f'The profit/loss to alchemise {item_name} is: {round(results["profit_or_loss"], 2)}')
    print(f'The hourly profit/loss to alchemise {item_name} is: {round(results["hourly"], 2)}')
    print(f'The daily profit/loss to alchemise {item_name} is: {round(results["daily"], 2)}')