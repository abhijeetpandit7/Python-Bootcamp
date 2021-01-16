from data import MENU, resources

def handleReport():
    """Show available resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def isAvailable(beverage):
    """Checks for requested beverage has required resources."""
    for ingredient in MENU[beverage]['ingredients']:
        if resources[ingredient] < MENU[beverage]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def transaction(beverage,q,d,n,p):
    """Check if payment received is sufficient. If yes, update resources to serve coffee."""
    receivedCoins = 0.25*q + 0.10*d + 0.05*n + 0.01*p
    cost = MENU[beverage]['cost']
    if receivedCoins < cost:
        print("“Sorry that's not enough money. Money refunded")
    else:
        print(f"Here is ${receivedCoins - cost:.2f} dollars in change")
        resources['money'] += cost
        for ingredient in MENU[beverage]['ingredients']:
            resources[ingredient] -= MENU[beverage]['ingredients'][ingredient]
        print(f"Here is your {beverage}☕️. Enjoy!")

def serveBeverage(beverage):
    """Ask user to enter coins and redirect to transaction"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    transaction(beverage,quarters,dimes,nickles,pennies)

def userInput():
    """Get input from user"""
    return input("​What would you like? (espresso/latte/cappuccino):").lower()

request = userInput()
while request != 'off':
    if request == 'report':
        handleReport()
    else:
        if isAvailable(request):
            serveBeverage(request)
    request = userInput()