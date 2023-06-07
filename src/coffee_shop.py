class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_cash(self, amount):
        self.till += amount

    def check_age(self, customer):
        return customer.age >= 16

    def check_energy(self, customer):
        return customer.energy_level <= 5

    def sell_drink(self, drink, customer):
        if customer.wallet >= drink.price and self.check_age(customer) and self.check_energy(customer):
            customer.buy_drink(drink)
            self.add_cash(drink.price)
        