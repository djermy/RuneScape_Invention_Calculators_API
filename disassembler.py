from api_fetcher import get_item_cost

# constants needed for calculator
CHARGES_PER_ITEM = 3.8
CORRUPTED_MAGIC_LOGS_ID = 40338
DIVINE_CHARGE_ID = 36390
ITEMS_PROCESSED_PER_HOUR = 60
MAGIC_LOGS_ID = 1513
SOAPSTONE_ID = 49458
LOGS_COMPS = {
    'simple parts': 0.99,
    'junk': 0.034
}
SOAPSTONE_COMPS = {
    'special': {
        'historic': 0.16,
        'classic': 0.4
        },
    'normal': {
        'simple parts': 1.0,
        'junk': 27.2
    }
}

# helper functions
def cost_of_charges():

    # returns cost of charges needed to process 1 item
    return CHARGES_PER_ITEM * cost_of_charge()

def cost_of_charge():

    # returns the current cost of 1 charge
    charge_cost = get_item_cost(DIVINE_CHARGE_ID) / 3000
    charge_cost = round(charge_cost, 2)

    return charge_cost

def validate_choice():

    # define list of 3 items
    options = define_options()

    # print options to screen along with index
    render_options(options)

    # take user choice
    choice = take_choice()

    # True or False, print error message if invalid
    valid = is_choice_valid(choice)
    
    # cycle until input is valid
    while not valid:
        render_options(options)
        choice = take_choice()
        valid = is_choice_valid(choice)

    return choice

def is_choice_valid(choice):
    VALID_CHARS = '012'

    if choice not in VALID_CHARS:
        print('Invalid selection please try again.')
        return False
    if len(choice) > 1:
        print('Input can only be 1 number! Please try again.')
        return False

    return True

def take_choice():
    return input('Please choose an item: ')

def render_options(options):
    print('Which item are you going to disassemble?')

    for index, item in enumerate(options):
        print(f'[{index}] {item}')

def define_options():
    return ['magic logs', 'corrupted magic logs', 'soapstone']

def get_item_value(choice):
    return get_item_cost(choice)