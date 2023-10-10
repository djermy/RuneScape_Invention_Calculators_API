from app.service.runescape.items import get_item_cost
from app.service.runescape.alchemy import scrape_alch_value
from app.service.calculators.calculator_utils import cost_of_charge
from app.database.store import store
import app.constants

def calculate_profit(item_name, item_id):

    item_cost = get_item_cost(item_id)
    alch_value = get_alch_value(item_name)
    cost_per_item = calculate_fuel_cost()

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = alch_value - total_cost_per_item
    hourly = (alch_value - total_cost_per_item) * app.constants.ITEMS_ALCHEMISED_PER_HOUR
    daily = hourly * 24

    return {
        'id': item_id,
        'profit_or_loss': profit_or_loss,
        'hourly': hourly,
        'daily': daily
    }

# main function
def alchemiser_calculator(item_id):
    '''
    Calculates profit/loss to alchemise the chosen item,
    and returns dictionary output.
    '''

    item_name = store.item_store.get(item_id)['name']
    profit = calculate_profit(item_name, item_id)

    return profit
    
# helper functions
def get_item_id(item_name):
    '''
    Take item_name and returns item_id.
    '''

    item_id = get_by_name(item_name)['id']
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

    cost_of_charges = app.constants.ALCHEMISER_CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = get_item_cost(app.constants.NATURE_RUNE_ID)
    cost_per_item = cost_of_charges + cost_of_nature_rune

    return cost_per_item

def print_result(results):
    # render output
    print(f'The profit/loss to alchemise {item_name} is: {round(results["profit_or_loss"], 2)}')
    print(f'The hourly profit/loss to alchemise {item_name} is: {round(results["hourly"], 2)}')
    print(f'The daily profit/loss to alchemise {item_name} is: {round(results["daily"], 2)}')