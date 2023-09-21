import api.service.calculators.calculator_utils as utils
from api.service.runescape.items import get_item_cost
from api.database.store import store 
import api.constants

def plank_maker(option_idx):
    '''
    Takes user selection and calculates singular, hourly and daily profit-
    for selected item.
    '''
    
    choice = option_idx
    profit = plank_calculator(choice)
    return profit

def plank_calculator(item_idx):
    '''
    Calculates the profit/loss to process chosen logs,
    and returns dictionary.
    '''

    # define chosen logs name via index
    logs_name = api.constants.PLANK_MAKER_INPUT[item_idx]
    logs_id = store.item_store.get_by_name(logs_name)[0] # get logs id
    logs_cost = get_item_cost(logs_id) # get logs cost
    
    # define plank type name via index
    plank_name = api.constants.PLANK_MAKER_OUTPUT[item_idx]
    plank_id = store.item_store.get_by_name(plank_name)[0] # get plank id
    plank_cost = get_item_cost(plank_id) # get plank cost

    # calculate the fuel cost to process 1 item
    cost_of_fuel = api.constants.PLANK_MAKER_CHARGES_PER_ITEM * utils.cost_of_charge()

    # total cost to process 1 set of logs
    cost_per_item = logs_cost + cost_of_fuel

    # profit/loss for 1 set of logs
    profit_or_loss = plank_cost - cost_per_item
    hourly = profit_or_loss * api.constants.PLANKS_MADE_PER_HOUR
    daily = hourly * 24
    
    return {
        'logs': logs_name,
        'plank': plank_name,
        'profit/loss': profit_or_loss,
        'hourly': hourly,
        'daily': daily
    }
