class Customer:
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level
        self.drink = []

    def reduce_cash(self, amount):
        self.wallet -= amount

    def increase_energy(self, energy):
        self.energy_level += energy

    def buy_drink(self, drink):
        self.drink.append(drink)
        self.reduce_cash(drink.price)
        self.increase_energy(drink.caffeine_level)