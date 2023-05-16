import requests, json, re

#API_DETAIL_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'
API_ITEMS_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={}&alpha={}&page={}'
API_QUERY = 'https://api.weirdgloop.org/exchange/history/rs/latest?id={}'

def get_item_cost(item_id):
    '''
    Fetch and return the current GE price of the given item_id.
    '''

    url = get_api_url(item_id)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw[str(item_id)]['price']
    cost = sanitisation_of_cost(cost)

    return cost

# helper functions
def get_api_url(item_id):
    return API_QUERY.format(item_id)

def sanitisation_of_cost(cost):
    return int(cost)