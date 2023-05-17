import sqlite3

def create_database():
    '''
    Create rs_items.db database and create items table.
    '''
    # connect to database
    conn = sqlite3.connect('rs_items.db')

    # create cursor
    cur = conn.cursor()

    # create items table
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS items
        (id INTEGER, name TEXT, category TEXT, category_id INTEGER, icon TEXT)
        '''
    )

    # close cursor and connection
    cur.close()
    conn.close()
    
    print('database created!')