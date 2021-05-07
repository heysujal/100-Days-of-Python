import sys
from data import MENU, resources


def is_sufficient(selected):
    water_required = MENU[selected]['ingredients']['water']
    if selected == "espresso":
        milk_required = 0
    else:
        milk_required = MENU[selected]['ingredients']['milk']
    coffee_required = MENU[selected]['ingredients']['coffee']

    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    is_water_sufficient = water_available >= water_required
    if selected == "espresso":
        is_milk_sufficient = True
    else:
        is_milk_sufficient = milk_available >= milk_required
    is_coffee_sufficient = coffee_available >= coffee_required

    # fact_list = [is_water_sufficient, is_milk_sufficient, is_coffee_sufficient]
    fact_dict = {
        "water":is_water_sufficient,
        "milk":is_milk_sufficient,
        "coffee":is_coffee_sufficient,

    }
    for key, value in fact_dict.items():
        if not value:
            print(f"Sorry there is not enough {key}")
            return False

    return True


is_machine_off: bool = False
while not is_machine_off:
    choice = input("What would you like?(espresso/latte/cappuccino): ")

    if choice == "off":
        is_machine_off = True
        sys.exit("Machine off")

    elif choice == "report":
        print(f"Water:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney: $"
              f"{resources['money']}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if is_sufficient(choice):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))

            amount_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            cost_of_coffee = MENU[choice]['cost']

            if amount_inserted >= cost_of_coffee:
                # Decreasing the resources quantity
                resources['water'] -= MENU[choice]['ingredients']['water']
                if not choice == "espresso":
                    resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                resources['money'] += MENU[choice]['cost']
                print(f"Here is ${round(amount_inserted - cost_of_coffee,2)} in change.")
                print(f"Here is your {choice} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
