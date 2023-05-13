from api_fetcher import get_nature_rune, get_divine_charge_cost, sanitisation_of_cost
from scraper import scrape_alch_value

# helper function
def cost_of_charge():
    '''
    Returns the cost of charges used to process 1 item.
    '''

    cost = sanitisation_of_cost(get_divine_charge_cost()) / 3000
    cost = round(cost, 2)

    return cost

def alchemiser_calculator():
    '''
    Calculates the singular and hourly profit/loss to alchemise the chosen item. 
    '''

    #item_cost = None
    #alch_value = None

    # constant of how many charges the machine uses per item
    CHARGES_PER_ITEM = 6

    # calculate the cost of machine fuels to process 1 item
    cost_of_charges = CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = sanitisation_of_cost(get_nature_rune())
    cost_per_item = round(cost_of_charges + cost_of_nature_rune, 2)

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = alch_value - total_cost_per_item

    # render output
    print(f'The profit/loss to alchemise this item is: {profit_or_loss}')
    print(f'The hourly profit/loss to alchemise this item is: {profit_or_loss * 25}')