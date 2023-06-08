from src.drink import Drink
class Customer:
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level


    def buy_drink(self, drink: Drink):
        self.wallet -= drink.price
        self.energy_level += drink.caffeine_level

        
    
