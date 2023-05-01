MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water_count": 300,
    "milk_count": 200,
    "coffee_count": 100,
    "money_count": 0
}


def check(water_need, milk_need, coffee_need):
    """Takes 3 inputs and tells if the machine can prepare the given order"""
    global resources
    b = ""
    need = []
    if resources["water_count"] >= water_need and resources["milk_count"] >= milk_need and resources["coffee_count"] >= coffee_need:
        process = True
    else:
        process = False
        if resources["water_count"] < water_need:
            need.append("water")
        elif resources["milk_count"] < milk_need:
            need.append("milk")
        elif resources["coffee_count"] < coffee_need:
            need.append("coffee")
        for i in need:
            b = b + "," + i
        print(f"Sorry there is not enough {b}.")
    return process


def coins():
    """Function to check if the user has paid enough, and how much change should be given to him."""
    quarter = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))
    paid = (quarter * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return paid


def requirements_alter(money_need, water_need, milk_need, coffee_need):
    """Function to alter the resources dictionary, after a successful trade."""
    resources["money_count"] = resources["money_count"] + money_need
    resources["water_count"] = resources["water_count"] - water_need
    resources["milk_count"] = resources["milk_count"] - milk_need
    resources["coffee_count"] = resources["coffee_count"] - coffee_need


def machine(water_need, milk_need, coffee_need, money_need):
    """The main function that is the base of the coffee machine."""
    global resources
    process = check(water_need, milk_need, coffee_need)
    if process is True:
        print("Please insert coins.")
        paid = coins()
        if paid >= money_need:
            print(f"Here is your change:{paid - money_need}")
            requirements_alter(money_need, water_need, milk_need, coffee_need)
            print("Here is your Expresso☕️")
        else:
            print("Sorry that's not enough money. Money refunded.")


def add():
    global resources
    milk_add = int(input("How much milk do you wish to add:"))
    water_add = int(input("How much water do you wish to add:"))
    coffee_add = int(input("How much coffee do you wish to add:"))
    money_take = int(input("How much money do you wish to withdraw:"))
    if money_take <= resources["money_count"]:
        resources["milk_count"] = resources["milk_count"] + milk_add
        resources["water_count"] = resources["water_count"] + water_add
        resources["coffee_count"] = resources["coffee_count"] + coffee_add
        resources["money_count"] = resources["money_count"] - money_take
    else:
        print("The machine does not have this much money.")


def expresso():
    global resources
    water_need = 50
    milk_need = 0
    coffee_need = 18
    money_need = 1.5
    machine(water_need, milk_need, coffee_need, money_need)


def latte():
    global resources
    water_need = 200
    milk_need = 150
    coffee_need = 24
    money_need = 2.5
    machine(water_need, milk_need, coffee_need, money_need)


def cappuccino():
    global resources
    water_need = 250
    milk_need = 100
    coffee_need = 24
    money_need = 3
    machine(water_need, milk_need, coffee_need, money_need)


a = True
while a is True:
    decision = input("What do you like(espresso/latte/cappuccino):").lower()
    if decision == "off":
        a = False
    elif decision == "report":
        print("Water:", resources["water_count"], "\nMilk:", resources["milk_count"], "\nCoffee:",
              resources["coffee_count"], "\nMoney:", resources["money_count"])
    elif decision == "expresso":
        expresso()
    elif decision == "latte":
        latte()
    elif decision == "cappuccino":
        cappuccino()
    elif decision == "add":
        add()
    else:
        print("Decision not clear")
