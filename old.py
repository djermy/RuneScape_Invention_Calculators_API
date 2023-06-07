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

# made for this:
#items = [{"icon":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_sprite.gif?id=9143","icon_large":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_big.gif?id=9143","id":9143,"type":"Bolts","typeIcon":"https://www.runescape.com/img/categories/Bolts","name":"Adamant bolts","description":"Adamant crossbow bolts.","current":{"trend":"neutral","price":177},"today":{"trend":"positive","price":"+5"},"members":"false"},{"icon":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_sprite.gif?id=31868","icon_large":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_big.gif?id=31868","id":31868,"type":"Bolts","typeIcon":"https://www.runescape.com/img/categories/Bolts","name":"Ascendri bolts","description":"Hydrix-tipped ascension crossbow bolts.","current":{"trend":"neutral","price":"7,815"},"today":{"trend":"neutral","price":0},"members":"true"},{"icon":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_sprite.gif?id=31881","icon_large":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_big.gif?id=31881","id":31881,"type":"Bolts","typeIcon":"https://www.runescape.com/img/categories/Bolts","name":"Ascendri bolts (e)","description":"On hitting a target, you may gain a deathmark for 15 seconds. While marked you gain 1% extra adrenaline per hit on any target. The mark can be refreshed while active.","current":{"trend":"neutral","price":"8,438"},"today":{"trend":"negative","price":"- 6"},"members":"true"},{"icon":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_sprite.gif?id=28465","icon_large":"https://secure.runescape.com/m=itemdb_rs/1684164740271_obj_big.gif?id=28465","id":28465,"type":"Bolts","typeIcon":"https://www.runescape.com/img/categories/Bolts","name":"Ascension bolts","description":"Very powerful bolts for use with the Ascension crossbow.","current":{"trend":"neutral","price":556},"today":{"trend":"neutral","price":0},"members":"true"}]

import json

CATEGORIES = {
    'Miscellaneous': 0,
    'Ammo': 1,
    'Arrows': 2,
    'Bolts': 3,
    'Construction materials': 4,
    'Construction products': 5,
    'Cooking ingredients': 6,
    'Costumes': 7,
    'Crafting materials': 8,
    'Familiars': 9,
    'Farming produce': 10,
    'Fletching materials': 11,
    'Food and Drink': 12,
    'Herblore materials': 13,
    'Hunting equipment': 14,
    'Hunting Produce': 15,
    'Jewellery': 16,
    'Mage armour': 17,
    'Mage weapons': 18,
    'Melee armour - low level': 19,
    'Melee armour - mid level': 20,
    'Melee armour - high level': 21,
    'Melee weapons - low level': 22,
    'Melee weapons - mid level': 23,
    'Melee weapons - high level': 24,
    'Mining and Smithing': 25,
    'Potions': 26,
    'Prayer armour': 27,
    'Prayer materials': 28,
    'Range armour': 29,
    'Range weapons': 30,
    'Runecrafting': 31,
    'Runes, Spells and Teleports': 32,
    'Seeds': 33,
    'Summoning scrolls': 34,
    'Tools and containers': 35,
    'Woodcutting product': 36,
    'Pocket items': 37,
    'Stone spirits': 38,
    'Salvage': 39,
    'Firemaking products': 40,
    'Archaeology materials': 41
    }

def load_clean_items_data(filename):
    '''
    Loads clean items JSON strings into and returns a list of dictionaries.
    '''

    with open(filename, 'r') as f:
        all_lines = f.readlines()
        items = [json.loads(line) for line in all_lines]
        return items

def filter_item_details(items):
    '''
    Takes a list of dictionaries and filters the desired values from each item-
    into a new list of dictionaries.
    '''

    cleaned_items = []
    for group in items:
        for item in group:
            cleaned_items.append({
                'id': item['id'],
                'name': item['name'],
                'category': item['type'],
                'category_id': CATEGORIES[item['type']],
                'icon': item['icon']
            })

    return cleaned_items

items = load_clean_items_data('cleaned.json')
cleaned_items = filter_item_details(items)
print(type(cleaned_items[0]))


'''
def disassembler_calculator(item):
    per_hour = 60
    comps_per_hour = {}
    if item.common:
        for comp in item.common:
            comps_per_hour[comp] = per_hour * item.common[comp]
    if item.rare:
        for comp in item.rare:
            comps_per_hour[comp] = per_hour * item.rare[comp]
    


magic_logs = {
    'common': {
        'simple parts': 0.99
    },
    'rare': {
        'living components': 0.01
    },
    'junk chance': 0.034
}

disassembler_calculator(magic_logs)
'''

def alchemiser_calculator():
    '''
    Calculates profit/loss to alchemise the chosen item,
    and provides several outputs. 
    '''

    # get user input and process it into components needed
    item_name = get_user_input()

    item_id = id_grabber(item_name)
    if item_id == None:
        print('Error item not found!')
        print('Perhaps you mispelled it?')
        return alchemiser_calculator()

    item_cost = get_item_cost(item_id)
    alch_value = scrape_alch_value(item_name)

    # check alch_value was properly obtained
    if type(alch_value) == str:
        print(alch_value)
        print('Please try again')
        return alchemiser_calculator()

    # calculate the cost of machine fuels to process 1 item
    cost_of_charges = constants.ALCHEMISER_CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = get_item_cost(constants.NATURE_RUNE_ID)
    cost_per_item = round(cost_of_charges + cost_of_nature_rune, 2)

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = alch_value - total_cost_per_item
    hourly = (alch_value - total_cost_per_item) * constants.ITEMS_ALCHEMISED_PER_HOUR
    daily = hourly * 24

    # for testing purposes
    # render output
    print(f'The profit/loss to alchemise this item is: {round(profit_or_loss, 2)}')
    print(f'The hourly profit/loss to alchemise this item is: {round(hourly, 2)}')
    print(f'The daily profit/loss to alchemise this item is: {round(daily, 2)}')



# from calculate comp value
    # for testing purposes only
    print(f'the value of a historic from a small crate is: {small_historic_comp_value}')
    print(f'the value of a historic from a large crate is: {large_historic_comp_value}')
    print(f'the value of a classic from a small crate is: {small_classic_comp_value}')
    print(f'the value of a classic from a large crate is: {large_classic_comp_value}')

# from calculate daily crates
    # for test purposes only
    print(f'number of daily historic = {daily_historic}\nnumber of daily classic = {daily_classic}')
    print(f'number of daily small historic = {daily_small_historic}\nnumber of daily small classic = {daily_small_classic}')
    print(f'number of daily large historic = {daily_large_historic}\nnumber of daily large classic = {daily_large_classic}')

# from dis calculator
    '''
        # get number of daily empty divine charges
        daily_empty_charges = calculate_empty_charges_per_day(constants.SOAPSTONE_COMPS)

        # get number of daily comps
        daily_historic_comps, daily_classic_comps = calculate_daily_soapstone_comps()
        
        # get number of crates made per day
        daily_crates = calculate_daily_crates(daily_historic_comps, daily_classic_comps)

        # get value of comps for all 4 crates
        comp_values = calculate_comp_value()

        # get best crate type and value for both comps
        best_crates = calculate_best_crate(comp_values)
        '''