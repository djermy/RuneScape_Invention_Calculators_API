from api_fetcher import get_item_cost
import constants

# helper functions
def cost_of_charges():

    # returns cost of charges needed to process 1 item
    return constants.CHARGES_PER_ITEM * cost_of_charge()

def cost_of_charge():

    # returns the current cost of 1 charge
    charge_cost = get_item_cost(constants.DIVINE_CHARGE_ID) / 3000
    charge_cost = round(charge_cost, 2)

    return charge_cost

def validate_choice():
    '''
    Prints options to user and takes and ensures input is valid before returning it.
    '''

    # print options to screen along with index
    render_options()

    # take user choice
    choice = input('Please choose an item: ')

    # True or False, print error message if invalid
    valid = is_choice_valid(choice)
    
    # cycle until input is valid
    while not valid:
        render_options()
        choice = input('Please choose an item: ')
        valid = is_choice_valid(choice)

    return choice

def is_choice_valid(choice):
    valid_choice = [str(idx) for idx in range(len(constants.ITEMS))]

    if choice not in valid_choice:
        print('Invalid selection please try again.')
        return False
    if len(choice) > 1:
        print('Input can only be 1 number! Please try again.')
        return False

    return True

def render_options():
    print('Which item are you going to disassemble?')

    for index, item in enumerate(constants.ITEMS):
        print(f'[{index}] {item}')

def get_item_value(choice):
    return get_item_cost(choice)

print(constants.ITEMS[int(validate_choice())])