# Tutorial https://replit.com/@appbrewery/coffee-machine-start

profit = 0

from data import resources
from data import MENU

def print_report():
    """ print report """
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money:  ${profit}")

def is_resource_sufficient(order):
    """ check if resources is enough to make coffee or not """
    is_enough = True
    for item in resources:
        if item not in order:
            continue
        if order[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            is_enough = False
    return is_enough

def process_counts():
    """ return the total calculated from coins inserted """
    print("Please insert coins.")
    total = int(input("how many quarter? :")) * .25
    total += int(input(f"how many dimes? (inserted ${total}):")) * .10
    total += int(input(f"how many quarter? (inserted ${total}):")) * .05
    total += int(input(f"how many quarter? (inserted ${total}):")) * .01
    return total

def is_transaction_success(received_money, cost) :
    """ return when the payment is accepted """
    if received_money >= cost:
        global profit
        profit += cost

        change = round(received_money - cost, 2)
        if change > 0 :
            print(f"Here is ${change} dollars in change")

        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(name, order) :
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {name} ☕")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off" or choice == "close":
        break
    if choice == "report":
        print_report()
        continue
    elif choice not in MENU:
        print("choose (espresso/latte/cappuccino) only")
        continue

    drink = MENU[choice]
    if not is_resource_sufficient(drink["ingredients"]):
        continue

    print(f"{choice} cost ${drink['cost']}")
    payment = process_counts()
    if not is_transaction_success(payment, drink["cost"]):
        continue

    make_coffe(choice, drink["ingredients"])

