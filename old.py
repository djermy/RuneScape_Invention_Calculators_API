# This file is for old code that may be reintroduced later, as well as to act
# as a backup and archive.

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

def get_nature_rune():
    '''
    Fetch and return the current GE price of nature rune.
    '''

    url = get_api_url(NATURE_RUNE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw[str(NATURE_RUNE_ID)]['price']

    # items below value of 10k, return as 'int' helper function needs 'str'
    if isinstance(cost, int):
        cost = str(cost)

    return cost

def get_divine_charge_cost():
    '''
    Fetch and return the current GE price of divine charge.
    '''

    url = get_api_url(DIVINE_CHARGE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw[str(DIVINE_CHARGE_ID)]['price']

    return cost

url = 'https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json'
url += '?category=' + str(category)
url += '&alpha=' + alphabet[letter]
url += '&page=' + str(page)