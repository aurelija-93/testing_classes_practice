import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Peter", 10.00, 45, 5)

    def test_customer_has_name(self):
        self.assertEqual("Peter", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(45, self.customer.age)
    
    def test_customer_has_energy_level(self):
        self.assertEqual(5, self.customer.energy_level)

    def test_reduce_cash(self):
        self.customer.reduce_cash(3.95)
        self.assertEqual(6.05, self.customer.wallet)

    def test_increase_energy(self):
        self.customer.increase_energy(2)
        self.assertEqual(7, self.customer.energy_level)

    def test_buy_drink(self):
        self.drink = Drink("Mocha", 3.95, 2)
        self.customer.buy_drink(self.drink)
        self.assertEqual(1, len(self.customer.drink))
        self.assertEqual(6.05, self.customer.wallet)