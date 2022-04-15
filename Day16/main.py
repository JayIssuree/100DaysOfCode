from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class CoffeeMachine():
    def __init__(self):
        self.is_on = True
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def turn_off(self):
        self.is_on = False

    def run(self):
        while self.is_on:
            order = self.prompt_user()
            if order == "off":
                self.turn_off()
            elif order == "report":
                self.print_report()
            else:
                drink = self.menu.find_drink(order)
                if self.coffee_maker.is_resource_sufficient(drink) and self.make_payment(drink.cost):
                    self.make_drink(drink)

    def prompt_user(self):
        order = input("What would you like? (" + self.menu.get_items() + "): ")
        return order

    def print_report(self):
        self.coffee_maker.report()
        self.money_machine.report()

    def make_drink(self, drink):
        self.coffee_maker.make_coffee(drink)

    def make_payment(self, cost):
        return self.money_machine.make_payment(cost)

        
cof_mac = CoffeeMachine()
cof_mac.run()