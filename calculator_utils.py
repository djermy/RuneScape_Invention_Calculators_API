from api_fetcher import get_item_cost
import constants

# helper function
def cost_of_charge():
    '''
    Returns the cost of 1 charge used to process items.
    '''

    charge_cost = get_item_cost(constants.DIVINE_CHARGE_ID) / 3000
    charge_cost = round(charge_cost, 2)

    return charge_cost