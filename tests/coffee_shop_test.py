import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Jitters", 100, {
            "Mocha": 2,
            "Latte": 3,
            "Hot chocolate": 4,
            "Tea": 5
            },
            ["Bagel", "Sandwich", "Croissant", "Cake"])
    def test_shop_has_name(self):
        self.assertEqual("The Jitters", self.coffee_shop.name)
    
    def test_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_shop_has_drinks(self):
        self.assertEqual({
            "Mocha": 2,
            "Latte": 3,
            "Hot chocolate": 4,
            "Tea": 5
            }, self.coffee_shop.drinks)

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
        self.customer = Customer("Peter", 3.00, 45, 5)
        self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual(100, self.coffee_shop.till)

    def test_sell_drink__age_too_low(self):
        self.drink = Drink("Latte", 4.15, 1)
        self.customer = Customer("Peter", 10.00, 15, 5)
        self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual(100.00, self.coffee_shop.till)

    def test_sell_drink__energy_too_high(self):
        self.drink = Drink("Latte", 4.15, 1)
        self.customer = Customer("Peter", 10.00, 45, 6)
        self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual(100.00, self.coffee_shop.till)

    def test_sell_food__successful(self):
        self.food = Food("Bagel", 4.50, 3)
        self.customer = Customer("Peter", 10.00, 45, 5)
        self.coffee_shop.sell_food(self.food, self.customer)
        self.assertEqual(104.50, self.coffee_shop.till)

    def test_sell_food__insufficient_funds(self):
        self.food = Food("Bagel", 4.50, 3)
        self.customer = Customer("Peter", 3.00, 45, 5)
        self.coffee_shop.sell_food(self.food, self.customer)
        self.assertEqual(100.00, self.coffee_shop.till)

    def test_total_stock(self):
        self.assertEqual(14, self.coffee_shop.total_stock())

    def test_stock_value(self):
        pass