'''
Creator: Shengbin Cui 
Date: July 28, 2023 
Day #15

Program Requirements 
    1. Print report 
    2. Check resources sufficient 
    3. Process coins 
    4. Check transaction successful 
    5. Make coffee 
'''
# Create a coffee menu 
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

# track profit 
profit = 0

# resource dict
resources = {
    "water": 300, 
    "milk": 200, 
    "coffee": 100,
}

# function for checking resources 
def is_resource_sufficient(order_ingredients):
    """
        Returns:
            True when order can be made, 
            False if ingredients are insufficient. 
    """
    is_enough = True
    for item in order_ingredients: 
        if order_ingredients[item] >= resources[item]: 
            print(f"Sorry there is not enough {item}. ")
            is_enough = False
    return is_enough

# function for processing coins 
def process_coins(): 
    """
        Returns the total calculated from coins inserted. 
    """
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25 
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05 
    total += int(input("How many pennies?: ")) * 0.01
    return total

# function for checking trading 
def is_transaction_successful(money_received, drink_cost):
    """
        Returns: 
            True when the payment is accepted 
            False if money is insufficient
    """
    if money_received >= drink_cost: 
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change. ")
        global profit 
        profit += drink_cost
        return True 
    else: 
        print("Sorry that's not enough money. Money refunded. ")
        return False 


# make coffee 
def make_coffee(drink_name, order_ingredients): 
    """
        Deduct the required ingredients from the resources. 
    """
    for item in order_ingredients: 
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ")
    
    
    
# track the status of the program 
is_on = True

# Run 
while is_on: 
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g") 
        print(f"Money: ${profit}")
    else: 
        drink = MENU[choice] 
        if is_resource_sufficient(drink["ingredients"]): 
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]): 
                make_coffee(choice, drink['ingredients'])

