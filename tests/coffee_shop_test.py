import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop:CoffeeShop = CoffeeShop("Molly's", 500.00)
        self.customer_over_16 = Customer("Kia", 400.00, 23, 0)
        self.customer_under_16 = Customer("Trish", 300.00, 13, 10)
        self.customer_shaking = Customer("Robert", 700.87, 45, 310)
        self.drink_americano = Drink("Americano", 8, 50)


    def test_coffee_shop_got_name(self):
        self.assertEqual("Molly's", self.coffee_shop.name)
    
    def test_coffee_shop_got_till(self):
        self.assertEqual(500.00, self.coffee_shop.till)

    # def test_coffee_shop_got_drinks(self):
    #     self.assertEqual(("Americano", "Espresso", "Latte"), self.coffee_shop.drinks)

    def test_coffee_shop_cash_for_sold_drink(self):
        self.assertEqual(500, self.coffee_shop.till)

    def test_customer_is_over_16(self):
        self.assertEqual(True, self.coffee_shop.customer_is_over_16(self.customer_over_16))
    
    def test_customer_is_not_over_16(self):
        self.assertEqual(False, self.coffee_shop.customer_is_over_16(self.customer_under_16))

    def test_sell_drink_to_customer_over_16(self):
        self.coffee_shop.sell_drink(self.drink_americano, self.customer_over_16)
        self.assertEqual(508.00, self.coffee_shop.till)
        self.assertEqual(392.00, self.customer_over_16.wallet)
    
    def test_do_not_sell_drink_to_customer_under_16(self):
        self.coffee_shop.sell_drink(self.drink_americano, self.customer_under_16)
        self.assertEqual(500, self.coffee_shop.till)
        self.assertEqual(300.00, self.customer_under_16.wallet)

    def test_customer_not_too_much_caffeine(self):
        self.assertEqual(False, self.coffee_shop.customer_too_much_caffeine(self.customer_over_16))
    
    def test_customer_too_much_caffeine(self):
        self.assertEqual(True, self.coffee_shop.customer_too_much_caffeine(self.customer_shaking))