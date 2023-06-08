import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sofia", 289, 18, 0)

    def test_customer_got_name(self):
        self.assertEqual("Sofia", self.customer.name)
    
    def test_customer_got_wallet(self):
        self.assertEqual(289, self.customer.wallet)
    
    def test_customer_bought_drink(self):
        self.assertEqual(289, self.customer.wallet)

    def test_customer_got_age(self):
        self.assertEqual(18, self.customer.age)

    def test_customer_got_energy_level(self):
        self.assertEqual(0, self.customer.energy_level)
