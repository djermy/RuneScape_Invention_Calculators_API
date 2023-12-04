import app.constants as constants
import sqlite3

"""
item_store.py

interface
---------
get(item_id)
get_all()
create(item)
update(item)
delete(item)

item
----
id: int
name: str
category: str
category_id: int
icon: str
"""

class Item_Store:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
    """        
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def close(self):
        self.cur.close()
        self.conn.close()
    """
    def get(self, item_id):
        get_query = """
            SELECT
                id,
                name,
                category,
                category_id,
                icon
            FROM
                items
            WHERE
                id = ?;
        """

        self.cur.execute(get_query, (item_id,))

        response = self.cur.fetchone()

        if not response:
            return None

        return response

    def get_by_name(self, item_name):
        get_query = """
            SELECT
                id,
                name,
                category,
                category_id,
                icon
            FROM
                items
            WHERE
                name = ?;
        """
    
        self.cur.execute(get_query, (item_name,))
    
        response = self.cur.fetchone()
        if not response:
            return None
    
        return response
    
    def get_all(self):
        get_all_query = """
            SELECT
                id,
                name,
                category,
                category_id,
                icon
            FROM
                items
            ;
        """
    
        self.cur.execute(get_all_query)
    
        response = self.cur.fetchall()
    
        if not response:
            return None

        return response 
    
    def create(self, item):
        insert_query = """
            INSERT INTO items
                (id, name, category, category_id, icon) 
            VALUES
                (?, ?, ?, ?, ?);
            """
    
        item_tuple = (
            item['id'],
            item['name'],
            item['category'],
            item['category_id'],
            item['icon'],
        )
    
        self.cur.execute(insert_query, item_tuple)
        self.conn.commit()
    
    def update(self, item):
        insert_query = """
            UPDATE items
            SET
                id = ?,
                name = ?,
                category = ?,
                category_id = ?,
                icon = ?
            WHERE
                id = ?;
            """
    
        item_tuple = (
            item['id'],
            item['name'],
            item['category'],
            item['category_id'],
            item['icon'],
            item['id'],
        )
    
        self.cur.execute(insert_query, item_tuple)
        self.conn.commit()
    
    def upsert(self, item):
        existing_item = self.get(item['id'])
        response = None
        if existing_item:
            response = self.update(item)
        else:
            response = self.create(item)
    
        return response
    
    def delete(self, item):
        delete_query = """
            DELETE FROM items
            WHERE
                id = ?;
            """
    
        self,cur.execute(delete_query, (item['id'],))
        self.conn.commit()
    
    def sanitise(self, unsanitised_item):
        item = unsanitised_item
        return {
            'id': item['id'],
            'name': item['name'],
            'category': item['type'],
            'category_id': constants.CATEGORIES[item['type']],
            'icon': item['icon']
        }