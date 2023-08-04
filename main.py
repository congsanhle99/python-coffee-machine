from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

# 1. user asking
# customer_choice = input(f"What would you like? {item_menu.get_item()}> ")

# 2. check machine ON - OFF
# machine_ON = True

# 3. print report
# coffee_machine.report()
# money_machine.report()


def report():
    coffee_machine.report()
    money_machine.report()


machine_ON = True
while machine_ON:
    customer_choice = input(f"\nType 'report' to see if the ingredients are enough!"
                            f"\nType 'off' to turn off the machine!" +
                            f"\nType what would you like? {item_menu.get_item()}>\n").lower()
    if customer_choice == "report":
        report()
    elif customer_choice == "off":
        machine_ON = False
    else:
        drink = item_menu.find_drink(customer_choice)
        if coffee_machine.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)
        else:
            break
