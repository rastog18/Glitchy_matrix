from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

obj1 = Menu()
obj2 = CoffeeMaker()
obj3 = MoneyMachine()
items = obj1.get_items()

machine = True

while machine is True:
    decision = input(f"Enter the drink you wish to buy: {items}").lower()
    if decision == "report":
        obj2.report()
        obj3.report()
    elif decision == "off":
        machine = False
    else:
        drink = obj1.find_drink(decision)
        requirements = obj2.is_resource_sufficient(drink)
        if requirements is True:
            payment = obj3.make_payment(drink.cost)
            if payment is True:
                obj2.make_coffee(drink)
