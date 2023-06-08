from src.customer import Customer

class CoffeeShop:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        # self.drinks = drinks

    def sell_drink(self, drink, customer: Customer):
        if self.customer_is_over_16(customer):
            customer.buy_drink(drink)
            self.cash_for_drink_sold(drink.price)

    def cash_for_drink_sold(self, amount):
        self.till += amount

    def customer_is_over_16(self, customer: Customer):
        return customer.age >= 16 
    
    def customer_too_much_caffeine(self, customer: Customer):
        return customer.energy_level >= 300

    
