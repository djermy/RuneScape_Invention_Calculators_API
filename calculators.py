from api_fetcher import get_item_cost
from scraper import scrape_alch_value
from user_input import get_user_input
from database_handler import id_grabber

NATURE_RUNE_ID = 561
DIVINE_CHARGE_ID = 36390

# helper function
def cost_of_charge():
    '''
    Returns the cost of charges used to process 1 item.
    '''

    charge_cost = get_item_cost(DIVINE_CHARGE_ID) / 3000
    charge_cost = round(charge_cost, 2)

    return charge_cost

# main functions
def alchemiser_calculator():
    '''
    Calculates profit/loss to alchemise the chosen item,
    and provides several outputs. 
    '''

    # get user input and process it into components needed
    item_name = get_user_input()
    item_id = id_grabber(item_name)
    item_cost = get_item_cost(item_id)
    alch_value = scrape_alch_value(item_name)

    # constant of how many charges the machine uses per item
    CHARGES_PER_ITEM = 6

    # calculate the cost of machine fuels to process 1 item
    cost_of_charges = CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = get_item_cost(NATURE_RUNE_ID)
    cost_per_item = round(cost_of_charges + cost_of_nature_rune, 2)

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = alch_value - total_cost_per_item
    hourly = (alch_value - total_cost_per_item) * 25
    daily = hourly * 24

    # render output
    print(f'The profit/loss to alchemise this item is: {profit_or_loss}')
    print(f'The hourly profit/loss to alchemise this item is: {hourly}')
    print(f'The daily profit/loss to alchemise this item is: {daily}')

alchemiser_calculator()