import requests, json, re

API_DETAIL_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'
NATURE_RUNE_ID = 561
DIVINE_CHARGE_ID = 36390

def get_nature_rune():
    '''
    Fetch and return the current GE price of nature rune.
    '''

    url = get_detail_url(NATURE_RUNE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw['item']['current']['price']

    # items below value of 10k, return as 'int' helper function needs 'str'
    if isinstance(cost, int):
        cost = str(cost)

    return cost

def get_divine_charge_cost():
    '''
    Fetch and return the current GE price of divine charge.
    '''

    url = get_detail_url(DIVINE_CHARGE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw['item']['current']['price']

    return cost

# helper functions
def get_detail_url(item_id):
    return API_DETAIL_QUERY.format(item_id)

def sanitisation_of_cost(cost):
    '''
    Converts cost string returned from api into an integer.
    '''
    
    multiplier = 1
    metrics = ['', 'k', 'm', 'b', 't', 'q']

    metric_group = re.search(r'\D$', cost)
    if metric_group:
        metric = metric_group.group()
        multiplier = 1000 ** metrics.index(metric.lower())

    cost_group = re.search(r'^[\d\.]+', cost)
    if cost_group:
        cost = cost_group.group()
        cost = round(float(cost) * multiplier)
        return int(cost)