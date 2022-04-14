# -*- coding: utf-8 -*-
import Data

is_on = True

def prompt_user():
    coffee_choice = raw_input("What would you like? (espresso/latte/cappuccino): ")
    return coffee_choice

def turn_off():
    global is_on
    is_on = False

def get_resource(resource):
    return Data.resources[resource]

def get_drink(drink):
    return Data.MENU[drink]

def print_report():
    water = str(get_resource("water"))
    milk = str(get_resource("milk"))
    coffee = str(get_resource("coffee"))
    money = str(get_resource("money"))
    water_message = "Water: " + water + "ml\n"
    milk_message = "Milk: " + milk + "ml\n"
    coffee_message = "Coffee: " + coffee + "g\n"
    money_message = "Money: $" + money
    message = water_message + milk_message + coffee_message + money_message
    print(message)

def select_option():
    selection = prompt_user()
    if selection == "off":
        turn_off()
    elif selection == "report":
        print_report()
    elif check_resources(selection):
        process_transaction(selection)

def check_resources(drink):
    if not enough_resource(drink, "coffee"):
        print("Sorry, there is not enough coffee")
        return False
    elif not enough_resource(drink, "water"):
        print("Sorry, there is not enough water")
        return False
    elif not enough_resource(drink, "milk"):
        print("Sorry, there is not enough milk")
        return False
    else:
        return True
    
def enough_resource(drink, ingredient):
    return get_resource(ingredient) >= get_drink(drink)["ingredients"][ingredient]

def process_coins():
    quarters = int(raw_input("How many quarters?: "))
    dimes = int(raw_input("How many dimes?: "))
    nickles = int(raw_input("How many nickles?: "))
    pennies = int(raw_input("How many pennies?: "))
    total = float((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies)/100
    return total

def process_transaction(drink):
    payment = process_coins()
    drink_cost = get_drink(drink)["cost"]
    if payment >= drink_cost:
        Data.resources["money"] += drink_cost
        change = str(round(float(payment - drink_cost), 2))
        print("Here is $" + change + " dollars in change.")
        make_coffee(drink)
    else:
        print("Sorry that is not enough money. Money refunded.")

def make_coffee(drink):
    remove_resource("water", get_drink(drink)["ingredients"]["water"])
    remove_resource("milk", get_drink(drink)["ingredients"]["milk"])
    remove_resource("coffee", get_drink(drink)["ingredients"]["coffee"])
    print("Here is your " + drink + ". Enjoy!")

def remove_resource(resource, amount):
    Data.resources[resource] -= amount

while is_on:
    select_option()
