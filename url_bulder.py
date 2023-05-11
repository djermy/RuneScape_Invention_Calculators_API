BASE_URL = 'https://runescape.wiki/w/{}'

def url_builder(item_name):
    '''
    Generates RS wiki url for the item given.
    '''

    return BASE_URL.format(item_name)