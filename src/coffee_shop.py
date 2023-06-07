class CoffeeShop:
    def __init__(self, name, till, drinks, food):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food = food

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

    def sell_food(self, food, customer):
        if customer.wallet >= food.price:
            customer.buy_food(food)
            self.add_cash(food.price)