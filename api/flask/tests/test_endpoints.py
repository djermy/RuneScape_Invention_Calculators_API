import unittest, os, copy
from app import create_app
from app.database.store import get_store
from flask import current_app as app, g
import app.config as config
from tests.fixtures.items import items as fixture_items

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ['ENVIRONMENT'] = 'testing'
        cls.app = create_app()
        #cls.client = cls.app.test_client()
    
    def setUp(self):
        print('setup')
        with self.app.app_context():
            #self.client = self.app.test_client()
            self.store = get_store()
            print(g.store)
            self.store.connect()
            print(os.stat(config.TestingConfig.DB_PATH))
            for item in fixture_items:
                print(item)
                self.store.item_store.upsert(item)
        print('setup end')

    def tearDown(self):
        print('teardown')
        with self.app.app_context():
            get_store().close()
            g.pop('store', None)
        print(config.TestingConfig.DB_PATH)
        os.remove(config.TestingConfig.DB_PATH)
        print('teardown end')

    def test_items_endpoint(self):
        print('test1')
        new_item = copy.deepcopy(fixture_items[0])
        new_item["id"] = 4
        self.store.item_store.upsert(new_item)
        
    
        response = self.app.test_client().get('/items') # get response from test client
        result = response.get_json() # extract json from reponse object

        expected_keys = ['id', 'name', 'category', 'category_id', 'icon'] # expected keys of json objects
        
        self.assertEqual(200, response.status_code) # ensure response is OK
        for row in result:
            for key in row:
                self.assertIn(key, expected_keys)
        
        
        self.assertEqual(len(result), 4)

    def test_items_endpoint2(self):
        print('test2')
        response2 = self.app.test_client().get('/items') # get response from test client
        result2 = response2.get_json() # extract json from reponse object
        print(result2)
        expected_keys = ['id', 'name', 'category', 'category_id', 'icon'] # expected keys of json objects
        
        self.assertEqual(200, response2.status_code) # ensure response is OK
        for row in result2:
            for key in row:
                self.assertIn(key, expected_keys)
        
        
        self.assertEqual(len(result2), 3)
    

if __name__ == '__main__':
    unittest.main()