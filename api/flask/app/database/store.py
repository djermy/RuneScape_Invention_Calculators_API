from app.database.item_store import Item_Store
from app.constants import DB_PATH
import sqlite3
from flask import current_app as app, g

class Store:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connect()

    def __del__(self):
        self.close()

    def close(self):
        #self.cur.close()
        self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = self.dict_factory
        self.cur = self.conn.cursor()
        self.create_database()
        
        # sub stores
        self.item_store = Item_Store(self.conn, self.cur)


    def create_database(self):
        '''
        Create rs_items.db database.
        '''

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id integer PRIMARY KEY,
                name text NOT NULL,
                category text,
                category_id integer,
                icon text
            );
        ''')

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

def get_store():
    if 'store' not in g:
        db_path = app.config['DB_PATH']
        g.store = Store(db_path)
    
    return g.store