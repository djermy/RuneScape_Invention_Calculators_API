from api.flask.app.database.item_store import Item_Store
from api.flask.app.constants import DB_PATH
import sqlite3

class Store:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = self.dict_factory
        self.cur = self.conn.cursor()
        self.create_database()
        
        # sub stores
        self.item_store = Item_Store(self.conn, self.cur)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def close(self):
        self.cur.close()
        self.conn.close()

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

store = Store(DB_PATH)