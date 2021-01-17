from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

request = input(f"​What would you like? {menu.get_items()}: ").lower()
while request != 'off':
    if request == 'report':
        # Show CoffeMaker and MoneyMachine report
        coffee_maker.report()
        money_machine.report()
    else:
        # Check requested drink is in menu
        drink = menu.find_drink(request)
        if drink:
            # Check required resources are available
            if coffee_maker.is_resource_sufficient(drink):
                # Check money received
                if money_machine.make_payment(drink.cost):
                    # Deducts resources
                    coffee_maker.make_coffee(drink)
    request = input(f"​What would you like? {menu.get_items()}: ").lower()