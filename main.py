
profit = 0

from data import resources
def print_report():
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money:  ${profit}")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off" or choice == "close":
        break
    if choice == "report":
        print_report()

