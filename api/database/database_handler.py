import pandas as pd
import sqlite3
from service.runescape.json_cleaner import filter_item_details

JSON_PATH = 'service/runescape/items_json/'
DB_PATH = 'database/'

def database_handler():
    '''
    Create and populate database.
    '''
    
    create_database()

    # name of cleaned JSON data to be used
    filename = JSON_PATH + 'cleaned.json'

    df = load_data_into_dataframe(filename)
    populate_database(df)

def populate_database(df):
    '''
    Populate the database with the items data from the pandas dataframe.
    '''

    # connect to database
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')

    # fill database with dataframe data
    table_name = 'items'
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # close connection to database
    conn.close()

    print('Database has been filled!')

def load_data_into_dataframe(filename):
    '''
    Load data into and return pandas dataframe.
    '''
    
    data = filter_item_details(filename)
    df = pd.DataFrame(data)
    
    # sanitise data before returning DataFrame
    df = df.sort_values(by='id')
    df['name'] = df['name'].str.lower()

    return df

def id_grabber(item_name):
    '''
    Use given item name to query the database and return the matching items ID
    '''

    # ensures item_name is lowercase for database query
    item_name = item_name.lower()

    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()
    
    cur.execute('SELECT id FROM items WHERE name = ?', (item_name,))
    
    response = cur.fetchone()
    if response:
        cur.close()
        conn.close()
        return response[0]
    else:
        cur.close()
        conn.close()
        return None

# database startup
def create_database():
    '''
    Create rs_items.db database.
    '''

    # create and connect to database
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')

    # close connection to database
    conn.close()
    
    print('database created!')