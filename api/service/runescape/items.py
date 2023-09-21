from api.database.store import store
from api.constants import API_ITEMS_QUERY, WIKI_API_QUERY, JSON_PATH
import requests, json, re, time, os

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
    return WIKI_API_QUERY.format(item_id)

def sanitisation_of_cost(cost):
    return int(cost)

def get_all_items():
    '''
    Query the RS items database API .items endpoint and collect each items
    details and write them to raw.json file. 
    '''

    # number of categories on the .items API endpoint
    total_categories = 42

    # subcategories on the .items API endpoint
    alphabet_letters = 'abcdefghijklmnopqrstuvwxyz#'
    alphabet = []
    for letter in alphabet_letters:
        if letter == '#':
            alphabet.append('%23')
        else:
            alphabet.append(letter)

    # iterate over each category
    for category in range(0, total_categories):

        # iterate over each letter in the alphabet per category
        for letter in alphabet:
            page = 1
            while True:

                # sleep for 5 seconds between requests
                time.sleep(5)

                # make the url
                url = API_ITEMS_QUERY.format(x=str(category), y=letter, z=str(page))

                # make the request and convert the json string into a python dict
                res = requests.get(url)
                if res.text == '':
                    print(f'category {category} and letter {letter} page {page} [FAILED]')
                    break
                else:
                    print(f'category {category} and letter {letter} page {page}')
                dictionary = json.loads(res.text)
                
                # if there is no item in the API response, break the loop
                # else add the items to the items list
                if 'items' not in dictionary or len(dictionary['items']) == 0:
                    break
                #print(dictionary['items'])
                for unsanitised_item in dictionary['items']:
                    item = store.item_store.sanitise(unsanitised_item)
                    store.item_store.upsert(item)

                page += 1
