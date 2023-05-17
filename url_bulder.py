BASE_URL = 'https://runescape.wiki/w/{}'

def url_builder(item_name):
    '''
    Generates RS wiki url for the item given.
    '''
    
    item_name = item_name.replace(' ', '_')
    return BASE_URL.format(item_name)