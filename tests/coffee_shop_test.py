import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Jitters", 100, ["Mocha", "Latte", "Hot_chocolate", "Tea"])

    def test_shop_has_name(self):
        self.assertEqual("The Jitters", self.coffee_shop.name)
    
    def test_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_shop_has_drinks(self):
        self.assertEqual(["Mocha", "Latte", "Hot_chocolate", "Tea"], self.coffee_shop.drinks)

    def test_add_cash(self):
        self.coffee_shop.add_cash(3.95)
        self.assertEqual(103.95, self.coffee_shop.till)

    def test_check_age__return_True(self):
        self.customer = Customer("Peter", 10.00, 45, 5)
        over_sixteeen = self.coffee_shop.check_age(self.customer)
        self.assertEqual(True, over_sixteeen)

    def test_check_age__return_False(self):
        self.customer = Customer("Peter", 10.00, 15, 5)
        over_sixteeen = self.coffee_shop.check_age(self.customer)
        self.assertEqual(False, over_sixteeen)

    def test_sell_drink__successful(self):
        self.drink = Drink("Latte", 4.15, 1)
        self.customer = Customer("Peter", 10.00, 45, 5)
        self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual(104.15, self.coffee_shop.till)

    def test_sell_drink__insufficient_funds(self):
        self.drink = Drink("Latte", 4.15, 1)
        self.customer = Customer("Peter", 10.00, 45, 5)
        self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual(104.15, self.coffee_shop.till)
