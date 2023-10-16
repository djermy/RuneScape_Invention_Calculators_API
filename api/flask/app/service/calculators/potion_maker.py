import app.constants as constants
import app.service.calculators.calculator_utils as utils
from app.service.runescape.items import get_item_cost
from app.database.store import store

def potion_maker(option_idx):
    '''
    Takes user selection and calculates singular, hourly and daily profit-
    for selected item.
    '''
    
    choice = option_idx
    profit = potion_calculator(choice)
    return profit

def potion_calculator(item_idx):
    """
    Calculates the profit/loss to process chosen herbs,
    and returns dictionary
    """
    
    # define chosen herbs name via index
    herbs_name = constants.POTION_MAKER_HERBS[item_idx]
    herbs_id = store.item_store.get_by_name(herbs_name)['id'] # get herbs id
    herbs_cost = get_item_cost(herbs_id) # get herbs cost
    
    # define unf potion name via index
    potion_name = constants.POTION_MAKER_OUTPUT[item_idx]
    potion_id = store.item_store.get_by_name(potion_name)['id'] # get potion id
    potion_cost = get_item_cost(potion_id) # get potion cost

    # calculate the fuel cost to process 1 item
    cost_of_vial_of_water = get_item_cost(227) # vial of water id
    cost_of_fuel = constants.POTION_MAKER_CHARGES_PER_ITEM * utils.cost_of_charge()

    # total cost to process 1 herb/potion
    cost_per_item = herbs_cost + cost_of_vial_of_water + cost_of_fuel

    # profit/loss for 1 set of logs
    profit_or_loss = potion_cost - cost_per_item
    hourly = profit_or_loss * constants.POTIONS_MADE_PER_HOUR
    daily = hourly * 24
    
    return {
        'herbs': herbs_name,
        'potion': potion_name,
        'profit/loss': profit_or_loss,
        'hourly': hourly,
        'daily': daily
    }