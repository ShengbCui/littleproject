'''
Creater: Shengbin Cui 
Date: August 5, 2023 
Day #16 

Program Requirements 
    1. Print report 
    2. Check resources sufficient 
    3. Process coins 
    4. Check transaction successful 
    5. Make coffee 
'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker() 
my_money_machine = MoneyMachine()
my_coffee_menu = Menu()

is_on = True 

while is_on: 
    options = my_coffee_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else: 
        drink = my_coffee_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) == True:
            if my_money_machine.make_payment(drink.cost) == True: 
                my_coffee_maker.make_coffee(drink)
            