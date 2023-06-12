import json
import api.constants

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
                'category_id': constants.CATEGORIES[item['type']],
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