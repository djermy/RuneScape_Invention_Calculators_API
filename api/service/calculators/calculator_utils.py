from api.service.runescape.items import get_item_cost
import api.constants

# disassembler functions
def logs_calculator(item_name, daily, empty_divine_charge_value):
    '''
    Perform calculations for logs
    '''

    daily_empty_charges = calculate_empty_charges_per_day(api.constants.LOGS_COMPS)
    
    # value of empty divine charges per day
    daily_empty_charge_value = round(empty_divine_charge_value * daily_empty_charges, 2)
    
    # profit/loss per day/hour
    daily_profit = daily_empty_charge_value - daily
    hourly_profit = daily_profit / 24
    per_item_profit = hourly_profit / api.constants.ITEMS_DISASSEMBLED_PER_HOUR

    return {
        'single': per_item_profit,
        'hourly': hourly_profit,
        'daily': daily_profit
    }

def print_logs_calculator(logs_results, item_name):
    '''
    Prints results from the logs calculator.
    '''

    print(f'The profit/loss to disassemble {item_name} is: {round(per_item_profit, 2)}')
    print(f'The hourly profit/loss to disassemble {item_name} is: {round(hourly_profit, 2)}')
    print(f'The daily profit/loss to disassemble {item_name} is: {round(daily_profit, 2)}')

def soapstone_calculator(daily, empty_divine_charge_value):
    '''
    Perform calculations for soapstone.
    '''

    # get average number of daily empty divine charges made per day
    daily_empty_charges = calculate_empty_charges_per_day(api.constants.SOAPSTONE_COMPS)

    # get average number of daily comps
    daily_historic_comps, daily_classic_comps = calculate_daily_soapstone_comps()
    
    # get average number of crates made per day
    daily_crates = calculate_daily_crates(daily_historic_comps, daily_classic_comps)

    # crate values
    crates = crate_values()

    # get value of comps for all 4 crates
    comp_values = calculate_comp_value(crates)

    # get best crate type and value for both comps
    best_crates = calculate_best_crate(comp_values)

    # daily values of all historic and classic comps
    daily_historic_value = round(best_crates['historic']['value'] * daily_historic_comps, 2)
    daily_classic_value = round(best_crates['classic']['value'] * daily_classic_comps, 2)
    total_daily_comp_value = round(daily_historic_value + daily_classic_value, 2)

    # value of empty divine charges per day
    daily_empty_charge_value = round(empty_divine_charge_value * daily_empty_charges, 2)

    # total value
    total_daily_value = round(total_daily_comp_value + daily_empty_charge_value, 2)

    # profit/loss
    daily_profit_or_loss = round(total_daily_value - daily, 2)
    hourly = round(daily_profit_or_loss / 24, 2)
    single = round(hourly / api.constants.ITEMS_DISASSEMBLED_PER_HOUR)

    return {
        'historic': {
            'crate': best_crates["historic"]["crate"],
            'value': best_crates["historic"]["value"]
        },
        'classic': {
                'crate': best_crates["classic"]["crate"],
                'value': best_crates["classic"]["value"]
        },
        'profits': {
            'single': single,
            'hourly': hourly,
            'daily': daily_profit_or_loss
        }
    }

def print_soapstone_calculator(results):
    '''
    Print the results from the soapstone calculator.
    '''

    # print historic
    print(f'The best crate to make for historic components are', end='')
    print(f' {results["historic"]["crate"]}, with a component', end='')
    print(f' value of {results["historic"]["value"]}')
    
    # print classic
    print(f'The best crate to make for classic components are', end='')
    print(f' {results["classic"]["crate"]}, with a component', end='')
    print(f' value of {results["classic"]["value"]}')

    # print profits
    print('The below values assume you make the stated best crate for both components!')
    print(f'The profit or loss to disassemble soapstone is {results["profits"]["single"]}')
    print(f'The hourly profit or loss to disassemble soapstone is {results["profits"]["hourly"]}')
    print(f'The daily profit or loss to disassemble soapstone is {results["profits"]["daily"]}')

# disassembler helper functions
def calculate_daily_soapstone_comps():
    '''
    Calculates and returns 2 values: daily_historic, daily_classic.
    The average amount of daily historic and classic components found.
    '''

    comps = api.constants.SOAPSTONE_COMPS
    
    # divine charges made
    daily_empty_charges = calculate_empty_charges_per_day(comps)
    
    # historic components
    p_historic = comps['special']['historic']
    hourly_historic = api.constants.ITEMS_DISASSEMBLED_PER_HOUR * p_historic
    daily_historic = hourly_historic * 24
   
    # classic components
    p_not_historic = 1 - p_historic
    p_classic = p_not_historic * comps['special']['classic']
    hourly_classic = api.constants.ITEMS_DISASSEMBLED_PER_HOUR * p_classic
    daily_classic = hourly_classic * 24
    
    return daily_historic, daily_classic

def calculate_comp_value(crates):
    '''
    Calculates the values of historic and classic components and returns-
    them as a dictionary object.
    '''

    # calculate historic comp values
    # value of crate divided by comps needed to make the crate
    small_historic_comp_value = round(crates['historic']['small'] / api.constants.SMALL_CRATE_COMPS, 2)
    large_historic_comp_value = round(crates['historic']['large'] / api.constants.LARGE_CRATE_COMPS, 2)

    # calculate classic comp values
    small_classic_comp_value = round(crates['classic']['small'] / api.constants.SMALL_CRATE_COMPS, 2)
    large_classic_comp_value = round(crates['classic']['large'] / api.constants.LARGE_CRATE_COMPS, 2)

    component_values = {
        'historic': {
            'small_value': small_historic_comp_value,
            'large_value': large_historic_comp_value
        },
        'classic': {
            'small_value': small_classic_comp_value,
            'large_value': large_classic_comp_value
        }
    }

    return component_values

def calculate_daily_crates(daily_historic, daily_classic):
    '''
    Take daily historic and classic components from soapstone.
    Calculate the daily small and large historic and classic crates-
    made per day and return them as a dictionary object.
    '''

    # calculate daily small crates
    daily_small_historic = round(daily_historic / api.constants.SMALL_CRATE_COMPS, 2)
    daily_small_classic = round(daily_classic / api.constants.SMALL_CRATE_COMPS, 2)

    # calculate daily large crates
    daily_large_historic = round(daily_historic / api.constants.LARGE_CRATE_COMPS, 2)
    daily_large_classic = round(daily_classic / api.constants.LARGE_CRATE_COMPS, 2)

    return {
        'daily_small_historic': daily_small_historic,
        'daily_large_historic': daily_large_historic,
        'daily_small_classic': daily_small_classic,
        'daily_large_classic': daily_large_classic
    }

def crate_values():
    '''
    Gets and returns dictionary of crate values.
    '''

    # get the value of all 4 crates
    small_historic = get_item_cost(api.constants.SMALL_HISTORIC_CRATE_ID)
    large_historic = get_item_cost(api.constants.LARGE_HISTORIC_CRATE_ID)
    small_classic = get_item_cost(api.constants.SMALL_CLASSIC_CRATE_ID)
    large_classic = get_item_cost(api.constants.LARGE_CLASSIC_CRATE_ID)

    crates = {
        'historic': {
            'small': small_historic,
            'large': large_historic
        },
        'classic': {
            'small': small_classic,
            'large': large_classic
        }
    }
    
    return crates

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

    # compare historic comps
    # compare small and large components, which ever is more valueable is best
    if comp_values['historic']['small_value'] > comp_values['historic']['large_value']:
        best_crate['historic']['value'] = comp_values['historic']['small_value']
        best_crate['historic']['crate'] = 'small'
    else:
        best_crate['historic']['value'] = comp_values['historic']['large_value']
        best_crate['historic']['crate'] = 'large'

    # compare classic comps
    if comp_values['classic']['small_value'] > comp_values['classic']['large_value']:
        best_crate['classic']['value'] = comp_values['classic']['small_value']
        best_crate['classic']['crate'] = 'small'
    else:
        best_crate['classic']['value'] = comp_values['classic']['large_value']
        best_crate['classic']['crate'] = 'large'

    return best_crate

# generic helper functions
def cost_of_charge():
    '''
    Returns the cost of 1 charge used to process items.
    '''

    charge_cost = get_item_cost(api.constants.DIVINE_CHARGE_ID) / 3000
    charge_cost = round(charge_cost, 2)

    return charge_cost

def calculate_empty_charges_per_day(comps):
    '''
    Take dictionary of simple parts and junk values and returns average-
    number of divine charges made per day.
    '''

    p_junk = comps['junk']
    p_not_junk = 1 - p_junk
    p_simple = comps['simple parts']
    p_overall = p_not_junk * p_simple
    simple_parts_per_hour = api.constants.ITEMS_DISASSEMBLED_PER_HOUR * p_overall
    simple_parts_per_day = simple_parts_per_hour * 24
    empty_divine_charges_per_day = simple_parts_per_day / api.constants.SIMPLE_PARTS_PER_EMPTY_DIVINE_CHARGE

    return round(empty_divine_charges_per_day, 2)