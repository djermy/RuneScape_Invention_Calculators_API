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

def json_cleaner(filename, filename2):
    '''
    Takes 2 'complete' filename strings. Converts filename1 into filename2 by removing-
    empty lines.
    '''

    data = load_data(filename)
    cleaned_data = remove_empty_data(data)
    dump_clean_data(cleaned_data, filename2)

def filter_item_details(filename):
    '''
    Takes complete filename string of cleaned JSON file and processes it into desired data-
    ready to be inserted into database. Returns list of dicts.
    '''

    items = load_clean_items_data(filename)
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

# helper functions
def load_data(filename):
    '''
    Takes filename as string and returns the loaded JSON lines as list object.
    '''

    data = None
    with open(filename, 'r') as f:
        data = f.readlines()
    
    return data

def remove_empty_data(data):
    '''
    Takes list of JSON strings and removes empty list items.
    '''

    cleaned_data = [item for item in data if item != '[]\n']

    return cleaned_data

def dump_clean_data(cleaned_data, filename):
    '''
    Takes cleaned list of JSON strings and writes them to new file.
    WARNING this is in WRITE MODE!, if file exists it WILL be overwritten.
    '''

    with open(filename, 'w') as f:
        f.writelines(cleaned_data)
    
    print(f'{filename} has been successfully created in the current directory!')

def load_clean_items_data(filename):
    '''
    Loads clean items JSON strings into and returns a list of dictionaries.
    '''

    with open(filename, 'r') as f:
        all_lines = f.readlines()
        items = [json.loads(line) for line in all_lines]
        return items