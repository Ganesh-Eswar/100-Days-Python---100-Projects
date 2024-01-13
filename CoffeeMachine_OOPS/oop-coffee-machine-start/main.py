from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cfe_maker = CoffeeMaker()
money_mac = MoneyMachine()
while True:
    print("Welcome to the coffee machine")
    m1 = Menu()
    menu_items = m1.get_items()
    user_cfe = input(f"What do you want? {menu_items}: ")
    if user_cfe == 'off':
        break
    core_det = m1.find_drink(user_cfe)
    if core_det is None:
        break
    if user_cfe == "report":
        resource = cfe_maker.resources
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        money_mac.report()
    else:
        if cfe_maker.is_resource_sufficient(core_det) and money_mac.make_payment(core_det.cost):
            cfe_maker.make_coffee(core_det)
