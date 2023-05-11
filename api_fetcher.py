import requests
import json

API_DETAIL_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'
NATURE_RUNE_ID = 561
DIVINE_CHARGE_ID = 36390

def get_detail_url(item_id):
    return API_DETAIL_QUERY.format(item_id)

def get_nature_rune():
    '''
    Fetch and return the current GE price of nature rune.
    '''

    url = get_detail_url(NATURE_RUNE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw['item']['current']['price']

    return cost

def get_divine_charge():
    '''
    Fetch and return the current GE price of divine charge.
    '''

    url = get_detail_url(DIVINE_CHARGE_ID)
    api_query = requests.get(url)
    raw = json.loads(api_query.text)
    cost = raw['item']['current']['price']

    return cost