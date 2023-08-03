import os

JSON_PATH = 'service/runescape/items_json/'
DB_PATH = 'database/'

def rebuild_database():
    '''
    !DANGEROUS!
    Deletes database and related files it was build from.
    Rebuilds database from scratch.
    '''

    # delete database and json files
    try:
        os.remove(JSON_PATH + 'output.json')
        os.remove
    
    