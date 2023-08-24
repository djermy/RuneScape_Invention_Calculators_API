from api.service.runescape.json_cleaner import filter_item_details
import sqlite3

JSON_PATH = 'service/runescape/items_json/'
DB_PATH = 'database/'

# create_database builds the database if it doesn't exist.
def create_database():
    '''
    Create rs_items.db database.
    '''

    # create and connect to database
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id integer PRIMARY KEY,
            name text NOT NULL,
            category text,
            category_id integer,
            icon text
        );
    ''')

    # close connection to database
    cur.close()
    conn.close()
