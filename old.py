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