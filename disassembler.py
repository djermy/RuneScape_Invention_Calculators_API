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

    # get value of empty divine charge
    empty_divine_charge_value = get_item_cost(constants.EMPTY_DIVINE_CHARGE_ID)

    # calculate cost of machine fuel to process 1 item
    cost_of_charges = constants.DISASSEMBLER_CHARGES_PER_ITEM * cost_of_charge()
    
    # total cost to process 1 of the chosen item
    cost_per_item = round((item_cost + cost_of_charges), 2)

    # hourly and daily costs to process chosen item
    hourly = round((cost_per_item * constants.ITEMS_DISASSEMBLED_PER_HOUR), 2)
    daily = round((hourly * 24), 2)

    if item_name == 'soapstone':

        # get number of daily empty divine charges
        daily_empty_charges = calculate_empty_charges_per_day(constants.SOAPSTONE_COMPS)

        # get number of daily comps
        daily_historic_comps, daily_classic_comps = calculate_daily_soapstone_comps()
        
        # get number of crates made per day
        daily_crates = calculate_daily_crates(daily_historic_comps, daily_classic_comps)

        # get value of comps for all 4 crates
        comp_values = calculate_comp_value()

        # get best crate type and value for both comps
        best_crates = calculate_best_crate(comp_values)
    else:
        daily_empty_charges = calculate_empty_charges_per_day(
            constants.LOGS_COMPS,
        )
    
    # value of empty divine charges per day
    daily_empty_charge_value = round(empty_divine_charge_value * daily_empty_charges, 2)

    # profit/loss per day/hour
    daily_profit = daily_empty_charge_value - daily
    hourly_profit = daily_profit / 24
    per_item_profit = hourly_profit / constants.ITEMS_DISASSEMBLED_PER_HOUR


    # for test purposes
    print(f'The profit/loss to disassemble {item_name} is: {round(per_item_profit, 2)}')
    print(f'The hourly profit/loss to disassemble {item_name} is: {round(hourly_profit, 2)}')
    print(f'The daily profit/loss to disassemble {item_name} is: {round(daily_profit, 2)}')

def calculate_daily_soapstone_comps():
    '''
    Calculates and returns 2 values: daily_historic, daily_classic.
    The amount of daily historic and classic components found.
    '''

    comps = constants.SOAPSTONE_COMPS
    
    # divine charges made
    daily_empty_charges = calculate_empty_charges_per_day(comps)
    
    # historic components
    p_historic = comps['special']['historic']
    hourly_historic = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_historic
    daily_historic = hourly_historic * 24
   
    # classic components
    p_not_historic = 1 - p_historic
    p_classic = p_not_historic * comps['special']['classic']
    hourly_classic = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_classic
    daily_classic = hourly_classic * 24
    
    return daily_historic, daily_classic

def calculate_empty_charges_per_day(comps):
    p_junk = comps['junk']
    p_not_junk = 1 - p_junk
    p_simple = comps['simple parts']
    p_overall = p_not_junk * p_simple
    simple_parts_per_hour = constants.ITEMS_DISASSEMBLED_PER_HOUR * p_overall
    simple_parts_per_day = simple_parts_per_hour * 24
    empty_divine_charges_per_day = simple_parts_per_day / constants.SIMPLE_PARTS_PER_EMPTY_DIVINE_CHARGE

    return round(empty_divine_charges_per_day, 2)

def calculate_daily_crates(daily_historic, daily_classic):
    '''
    Take daily historic and classic components from soapstone.
    Calculate the daily small and large historic and classic crates-
    made per day and return them as a dictionary object.
    '''

    # calculate daily small crates
    daily_small_historic = round(daily_historic / constants.SMALL_CRATE_COMPS, 2)
    daily_small_classic = round(daily_classic / constants.SMALL_CRATE_COMPS, 2)

    # calculate daily large crates
    daily_large_historic = round(daily_historic / constants.LARGE_CRATE_COMPS, 2)
    daily_large_classic = round(daily_classic / constants.LARGE_CRATE_COMPS, 2)

    # for test purposes only
    print(f'number of daily historic = {daily_historic}\nnumber of daily classic = {daily_classic}')
    print(f'number of daily small historic = {daily_small_historic}\nnumber of daily small classic = {daily_small_classic}')
    print(f'number of daily large historic = {daily_large_historic}\nnumber of daily large classic = {daily_large_classic}')

    return {
        'daily_small_historic': daily_small_historic,
        'daily_large_historic': daily_large_historic,
        'daily_small_classic': daily_small_classic,
        'daily_large_classic': daily_large_classic
    }

def calculate_comp_value():
    '''
    Calculates and returns the values of historic and classic comps and returns-
    them as a dictionary object.
    '''

    # get the value of all 4 crates
    small_historic = get_item_cost(constants.SMALL_HISTORIC_CRATE_ID)
    large_historic = get_item_cost(constants.LARGE_HISTORIC_CRATE_ID)
    small_classic = get_item_cost(constants.SMALL_CLASSIC_CRATE_ID)
    large_classic = get_item_cost(constants.LARGE_CLASSIC_CRATE_ID)

    # calculate historic comp values
    small_historic_comp_value = round(small_historic / constants.SMALL_CRATE_COMPS, 2)
    large_historic_comp_value = round(large_historic / constants.LARGE_CRATE_COMPS, 2)

    # calculate classic comp values
    small_classic_comp_value = round(small_classic / constants.SMALL_CRATE_COMPS, 2)
    large_classic_comp_value = round(large_classic / constants.LARGE_CRATE_COMPS, 2)
    
    # for testing purposes only
    print(f'the value of a historic from a small crate is: {small_historic_comp_value}')
    print(f'the value of a historic from a large crate is: {large_historic_comp_value}')
    print(f'the value of a classic from a small crate is: {small_classic_comp_value}')
    print(f'the value of a classic from a large crate is: {large_classic_comp_value}')

    return {
        'small_historic_value': small_historic_comp_value,
        'large_historic_value': large_historic_comp_value,
        'small_classic_value': small_classic_comp_value,
        'large_classic_value': large_classic_comp_value
    }

def calculate_best_crate(comp_values):
    '''
    Takes dictionary object of component values for small and large crates-
    and returns a dictionary object of the most valuable component and which crate.
    '''

    best_crate = {
        'historic': {
            'value': None,
            'crate': None
        },
        'classic': {
            'value': None,
            'crate': None
        }
    }

    if comp_values['small_historic_value'] > comp_values['large_historic_value']:
        best_crate['historic']['value'] = comp_values['small_historic_value']
        best_crate['historic']['crate'] = 'small'
    else:
        best_crate['historic']['value'] = comp_values['large_historic_value']
        best_crate['historic']['crate'] = 'large'

    if comp_values['small_classic_value'] > comp_values['large_classic_value']:
        best_crate['classic']['value'] = comp_values['small_classic_value']
        best_crate['classic']['crate'] = 'small'
    else:
        best_crate['classic']['value'] = comp_values['large_classic_value']
        best_crate['classic']['crate'] = 'large'

    return best_crate

disassembler_calculator()