# 11-1. City, Country && 11-2. Population
import unittest
from city_functions import formatted_city_name

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        """Do city like 'Chengdu, China' work?"""
        city_name = formatted_city_name('chengdu', 'china')
        self.assertEqual(city_name, 'Chengdu, China')

    def test_city_country_population(self):
        """Do city like 'Santiago, Chile - population 5000000' work?"""
        city_country_population = formatted_city_name(
            'santiago', 'chile', '5000000')
        self.assertEqual(
            city_country_population, 'Santiago, Chile - population 5000000')
if __name__ == '__main__':
    unittest.main()