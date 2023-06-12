from api.constants import API_ITEMS_QUERY, WIKI_API_QUERY
import requests, json, re, time

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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # iterate over each category
    for category in range(0, total_categories):

        # iterate over each letter in the alphabet per category
        for letter in alphabet:
            is_end = False
            page = 1
            while not is_end:

                items = []

                # sleep for 5 seconds between requests
                time.sleep(5)

                # make the url
                url = API_ITEMS_QUERY.format(x=str(category), y=letter, z=str(page))

                # make the request and convert the json string into a python dict
                res = requests.get(url)
                dictionary = json.loads(res.text)

                # if there is no item in the API response, break the loop
                # else add the items to the items list
                if dictionary['items'] == []:
                    is_end = True
                else:
                    items += dictionary['items']

                print(len(items))
                print(f'category: {category}')
                print(f'letter: {letter}')
                print(f'page: {page}')
                page += 1

                # write items to a file for future filtering
                with open('output.json', 'a') as f:
                    json.dump(items, f)
                    f.write('\n')