DB_PATH = 'database/rs_items.db'
JSON_PATH = 'service/runescape/items_json/'
ALCHEMISER_CHARGES_PER_ITEM = 6
DISASSEMBLER_CHARGES_PER_ITEM = 3.8
PLANK_MAKER_CHARGES_PER_ITEM = 15
SIMPLE_PARTS_PER_EMPTY_DIVINE_CHARGE = 20
CORRUPTED_MAGIC_LOGS_ID = 40338
DIVINE_CHARGE_ID = 36390
EMPTY_DIVINE_CHARGE_ID = 41073
ITEMS = ['Magic logs', 'Corrupted magic logs', 'Soapstone']
PLANK_MAKER_INPUT = ['Logs', 'Oak logs', 'Willow logs', 'Teak logs', 'Maple logs',\
    'Acadia logs', 'Mahogany logs', 'Yew logs', 'Magic logs', 'Elder logs']
PLANK_MAKER_OUTPUT = ['Plank', 'Oak plank', 'Willow plank', 'Teak plank', 'Maple plank',\
    'Acadia plank', 'Mahogany plank', 'Yew plank', 'Magic plank', 'Elder plank']
ITEMS_DISASSEMBLED_PER_HOUR = 60
ITEMS_ALCHEMISED_PER_HOUR = 25
PLANKS_MADE_PER_HOUR = 40
MAGIC_LOGS_ID = 1513
NATURE_RUNE_ID = 561
SOAPSTONE_ID = 49458
SMALL_CRATE_COMPS = 100
LARGE_CRATE_COMPS = 1000
SMALL_HISTORIC_CRATE_ID = 50162
LARGE_HISTORIC_CRATE_ID = 50163
SMALL_CLASSIC_CRATE_ID = 50164
LARGE_CLASSIC_CRATE_ID = 50165
VALID_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890!&()/-+. '
VALID_NUMS = '0123456789'
API_ITEMS_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={x}&alpha={y}&page={z}'
WIKI_API_QUERY = 'https://api.weirdgloop.org/exchange/history/rs/latest?id={}'
LOGS_COMPS = {
    'simple parts': 0.99,
    'junk': 0.034
}
SOAPSTONE_COMPS = {
    'special': {
        'historic': 0.16,
        'classic': 0.04
    },
    'simple parts': 1.0,
    'junk': 0.272
}
CATEGORIES = {
    'Miscellaneous': 0,
    'Ammo': 1,
    'Arrows': 2,
    'Bolts': 3,
    'Construction materials': 4,
    'Construction products': 5,
    'Cooking ingredients': 6,
    'Costumes': 7,
    'Crafting materials': 8,
    'Familiars': 9,
    'Farming produce': 10,
    'Fletching materials': 11,
    'Food and Drink': 12,
    'Herblore materials': 13,
    'Hunting equipment': 14,
    'Hunting Produce': 15,
    'Jewellery': 16,
    'Magic armour': 17,
    'Magic weapons': 18,
    'Melee armour - low level': 19,
    'Melee armour - mid level': 20,
    'Melee armour - high level': 21,
    'Melee weapons - low level': 22,
    'Melee weapons - mid level': 23,
    'Melee weapons - high level': 24,
    'Mining and Smithing': 25,
    'Potions': 26,
    'Prayer armour': 27,
    'Prayer materials': 28,
    'Ranged armour': 29,
    'Ranged weapons': 30,
    'Runecrafting': 31,
    'Runes, Spells and Teleports': 32,
    'Seeds': 33,
    'Summoning scrolls': 34,
    'Tools and containers': 35,
    'Woodcutting product': 36,
    'Pocket items': 37,
    'Stone spirits': 38,
    'Salvage': 39,
    'Firemaking products': 40,
    'Archaeology materials': 41,
    'Wood spirits': 42,
    'Necromancy armour': 43
    }