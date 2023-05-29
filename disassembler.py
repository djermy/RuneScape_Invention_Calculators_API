from api_fetcher import get_item_cost
from database_handler import id_grabber
from calculator_utils import cost_of_charge
from user_input import validate_choice, is_choice_valid
import constants

def disassembler_calculator():

    # get users item index to disassemble
    choice = validate_choice()
    
    # define chosen items name via index
    item_name = constants.ITEMS[choice]
    
    # get item id
    item_id = id_grabber(item_name)

    # get current item cost
    item_cost = get_item_cost(item_id)

    # calculate cost of machine fuel to process 1 item
    cost_of_charges = constants.DISASSEMBLER_CHARGES_PER_ITEM * cost_of_charge()
    
    # total cost per item
    cost_per_item = round(item_cost + cost_of_charges, 2)