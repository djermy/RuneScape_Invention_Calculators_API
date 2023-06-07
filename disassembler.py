import calculator_utils as utils
from api_fetcher import get_item_cost
from database_handler import id_grabber
from user_input import validate_choice, is_choice_valid
import constants

def disassembler_calculator():
    '''
    Takes user selection and calculates singular, hourly and daily profit-
    for selected item.
    '''

    # get users item index to disassemble
    choice = validate_choice()
    
    # define chosen items name via index
    item_name = constants.ITEMS[choice]

    # get item id
    item_id = id_grabber(item_name)

    # get current item cost
    item_cost = get_item_cost(item_id)

    # calculate cost of machine fuel to process 1 item
    cost_of_charges = constants.DISASSEMBLER_CHARGES_PER_ITEM * utils.cost_of_charge()

    # total cost to process 1 of the chosen item
    cost_per_item = round((item_cost + cost_of_charges), 2)

    # hourly and daily costs to process chosen item
    hourly = round((cost_per_item * constants.ITEMS_DISASSEMBLED_PER_HOUR), 2)
    daily = round((hourly * 24), 2)

    # get value of 1 empty divine charge
    empty_divine_charge_value = get_item_cost(constants.EMPTY_DIVINE_CHARGE_ID)
    
    if item_name == 'soapstone':
        utils.soapstone_calculator(daily, empty_divine_charge_value)
    else:
        utils.logs_calculator(item_name, daily, empty_divine_charge_value)

disassembler_calculator()