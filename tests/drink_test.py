import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Coffee", 7, 50)

    def test_drink_got_name(self):
        self.assertEqual("Coffee", self.drink.name)
    
    def test_drink_got_price(self):
        self.assertEqual(7, self.drink.price)

    def test_drink_got_caffeine(self):
        self.assertEqual(50, self.drink.caffeine_level)