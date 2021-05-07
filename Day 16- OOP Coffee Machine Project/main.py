from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
clear = lambda: os.system('cls')



menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

is_machine_off = False

while not is_machine_off:
    clear()
    choice = input(f"What would you like? {menu_obj.get_items()}\n")
    # 
    if choice=="off":
        is_machine_off = True
    elif choice == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:

        selected_drink = menu_obj.find_drink(choice)
        if coffee_maker_obj.is_resource_sufficient(selected_drink):
            if money_machine_obj.make_payment(selected_drink.cost):
                coffee_maker_obj.make_coffee(selected_drink)



