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
    
    # total cost to process 1 of the chosen item
    cost_per_item = round(item_cost + cost_of_charges, 2)

    # hourly and daily costs to process chosen item
    hourly = round(cost_per_item * constants.ITEMS_DISASSEMBLED_PER_HOUR, 2)
    daily = round(hourly * 24, 2)

    if item_name == 'soapstone':
        comps = constants.SOAPSTONE_COMPS
        # divine
        divine_charges_per_day = calculate_divine_charges_per_day(comps)
        # historic
        p_historic = comps['special']['historic']
        historic_per_hour = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_historic
        historic_per_day = historic_per_hour * 24
        # classic
        p_not_historic = 1 - p_historic
        p_classic = p_not_historic * comps['special']['classic']
        classic_per_hour = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_classic
        classic_per_day = classic_per_hour * 24
    else:
        divine_charges_per_day = calculate_divine_charges_per_day(
            constants.LOGS_COMPS,
        )

def calculate_divine_charges_per_day(comps):
    p_junk = comps['junk']
    p_not_junk = 1 - p_junk
    p_simple = comps['simple parts']
    p_overall = p_not_junk * p_simple
    simple_parts_per_hour = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_overall
    simple_parts_per_day = simple_parts_per_hour * 24
    empty_divine_charges_per_day = simple_parts_per_day / constants.SIMPLE_PARTS_PER_EMPTY_DIVINE_CHARGE

    return empty_divine_charges_per_day