menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

recipe = []
def check_resources(drink, recipe):
    if  recipe[0] > resources["water"]:
        print(f"Not enough water to make {drink}")
        return False
    elif recipe[1] > resources["milk"]:
        print(f"Not enough milk to make {drink}")
        return False
    elif recipe[2] > resources["coffee"]:
        print(f"Not enough coffee to make {drink}")
        return False
    else:
        return True

def drink_menu(drink):
    recipe = []
    recipe.extend([menu[drink]["ingredients"]["water"], menu[drink]["ingredients"]["milk"], menu[drink]["ingredients"]["coffee"]])
    return recipe

def update_resources(drink, recipe):
    resources["water"] -= recipe[0]
    resources["milk"] -= recipe[1]
    resources["coffee"] -= recipe[2]
    resources["money"] += menu[drink]["cost"]

def count_coins(drink):
    qtrs = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    total = 0.25 * qtrs + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies

    if total > menu[drink]["cost"]:
        print(f"Here is the ${total - menu[drink]["cost"]:.2f} change. \n")
        print(f"Here is the {drink}. Enjoy. \n")
    elif total < menu[drink]["cost"]:
        print(f"You do not have enough money to purchase the {drink}.Here is the ${total} refunded back.")
    elif total == menu[drink]["cost"]:
        print(f"Here is the {drink}. Enjoy. \n")


continue_game = True
option = input("What would you like? (espresso/latte/cappuccino): ")
while continue_game:
    if option == "report":
        for k,v in resources.items():
            if k == "money":
                print(f"{(k.title())}:${v:.2f}")
            else:
                print(f"{(k.title())}:{v}")
    elif option == "off":
        continue_game = False
        break
    else:
        recipe = drink_menu(option)
        if check_resources(option, recipe):
            print(f"Your cost is : ${menu[option]["cost"]:.2f}. Please insert coins.")
            count_coins(option)
            update_resources(option, recipe)

    option = input("What would you like? (espresso/latte/cappuccino): ")




