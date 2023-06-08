import requests, re
from bs4 import BeautifulSoup

BASE_URL = 'https://runescape.wiki/w/{}'

def scrape_alch_value(item_name):
    '''
    Use item name to build url, scrape data and return the value.
    '''

    url = url_builder(item_name)
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, 'html.parser')
    table = soup.find('table', {'class': 'plainlinks rsw-infobox no-parenthesis-style infobox-item'})
    alch_value = 'Item either doesn\'t exist or is not alchemisable'
    if table == None or table.tbody == None:
        return alch_value
    for tr in table.tbody:
        if tr == None or tr.th == None or tr.th.a == None:
            continue
        if tr.th.a.text == 'High alch':
            alch_value_string = tr.td.text
            alch_value = int(re.sub('\D*', '', alch_value_string))
    
    return alch_value

# helper function
def url_builder(item_name):
    '''
    Generates RS wiki url for the item given.
    '''
    
    item_name = item_name.replace(' ', '_')
    return BASE_URL.format(item_name)