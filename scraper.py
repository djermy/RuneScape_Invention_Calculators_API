import requests
from bs4 import BeautifulSoup

# import helper functions
from user_input import get_user_input
from url_bulder import url_builder

def scrape_alch_value():
    '''
    Use item name to build url, scrape data and return the value.
    '''

    url = url_builder(get_user_input())
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
            alch_value = int(tr.td.text.replace(',', '').replace(' coins', ''))   
    
    return alch_value