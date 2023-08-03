import api.constants as constants
import sqlite3

"""
runescape_item.py

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

DB_PATH = 'database/'

def get(item_id):
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

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
    
    cur.execute(get_query, (item_id,))
    
    response = cur.fetchone()
    cur.close()
    conn.close()

    if not response:
        return None

    return response[0]

def get_by_name(item_name):
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

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
    
    cur.execute(get_query, (item_name,))
    
    response = cur.fetchone()
    cur.close()
    conn.close()

    if not response:
        return None

    return response[0]

def get_all():
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

    get_all_query = """
        SELECT
            id,
            name,
            category,
            category_id,
            icon
        FROM
            items;
    """
    
    cur.execute(get_all_query)
    
    response = cur.fetchall()
    cur.close()
    conn.close()

    if not response:
        return None

    return response

def create(item):
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

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

    cur.execute(insert_query, item_tuple)
    conn.commit()
    cur.close()
    conn.close()

def update(item):
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

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

    cur.execute(insert_query, item_tuple)
    conn.commit()
    cur.close()
    conn.close()

def upsert(item):
    existing_item = get(item['id'])
    response = None
    if existing_item:
        response = update(item)
    else:
        response = create(item)

    return response

def delete(item):
    conn = sqlite3.connect(DB_PATH + 'rs_items.db')
    cur = conn.cursor()

    delete_query = """
        DELETE FROM items
        WHERE
            id = ?;
        """

    cur.execute(delete_query, (item['id'],))
    conn.commit()
    cur.close()
    conn.close()

def sanitise(unsanitised_item):
    item = unsanitised_item
    return {
        'id': item['id'],
        'name': item['name'],
        'category': item['type'],
        'category_id': constants.CATEGORIES[item['type']],
        'icon': item['icon']
    }