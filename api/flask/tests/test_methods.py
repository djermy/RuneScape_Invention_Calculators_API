import unittest
from app import create_app
from app.service.calculators.calculator_utils import calculate_daily_crates,\
     calculate_empty_charges_per_day

class TestApp(unittest.TestCase):

    def test_calculate_daily_crates(self):
        expected = {
            'daily_small_historic': 5.0,
            'daily_large_historic': 0.5,
            'daily_small_classic': 0.5,
            'daily_large_classic': 0.05,
        }
    
        res = calculate_daily_crates(500, 50)  
        self.assertDictEqual(expected, res)

    def test_calculate_empty_charges_per_day(self):
        expected = 52.416
        fixture = {
            'special': {
                'historic': 0.16,
                'classic': 0.04,
            },
            'simple parts': 1.0,
            'junk': 0.272
        }

        res = calculate_empty_charges_per_day(fixture)
        self.assertEqual(expected, res)

    def test_calculate_empty_charges_per_day_2(self):
        expected = 0
        fixture = {
            'special': {
                'historic': 0,
                'classic': 0,
            },
            'simple parts': 0,
            'junk': 0
        }

        res = calculate_empty_charges_per_day(fixture)
        self.assertEqual(expected, res)

    def test_calculate_empty_charges_per_day_3(self):
        expected = 0
        fixture = {
            'special': {
                'historic': 1,
                'classic': 1,
            },
            'simple parts': 1,
            'junk': 1
        }

        res = calculate_empty_charges_per_day(fixture)
        self.assertEqual(expected, res)
if __name__ == '__main__':
    unittest.main()