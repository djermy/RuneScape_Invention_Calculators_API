from api.service.runescape.json_cleaner import filter_item_details
from api.database.item_store import Item_Store
import sqlite3

conn.row_factory = dict_factory
class Store:
    def __init__(self, db_path, json_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.conn.row_factory = self.dict_factory
        self.create_database()
        
        # sub stores
        self.item_store = Item_Store(conn, cur)

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