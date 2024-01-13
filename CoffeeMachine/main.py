from data import MENU


def user_coffee_details(name):
    needed_water = (MENU[name]['ingredients']).get('water', 0)
    needed_milk = (MENU[name]['ingredients']).get('milk', 0)
    needed_coffee = (MENU[name]['ingredients']).get('coffee', 0)
    cost = MENU[name]['cost']
    return needed_water, needed_milk, needed_coffee, cost


def user_total_cost(quarter, dime, nickle, pennies):
    return quarter*0.25 + dime*0.10 + nickle*0.05 + pennies*0.01


def can_buy(user_paid, actual_cost):
    if user_paid >= actual_cost:
        return True
    else:
        return False


def final_decision(coffee_type, buy, paid, cost):
    if not buy:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is {round(paid-cost,2)} in change.")
        print(f"Here is your {coffee_type} ☕. Enjoy!")


def machine_update(water, milk, coffee, cost, ini_water, ini_milk, ini_coffee, ini_cost):
    return ini_water-water, ini_milk-milk, ini_coffee-coffee, ini_cost+cost


def machine_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def is_sufficient(ini_water, ini_milk, ini_cfe, n_water, n_milk, n_cfe):
    sufficient = True
    if ini_water < n_water:
        sufficient = False
        print("Sorry not enough water!")
    if ini_milk < n_milk:
        sufficient = False
        print("Sorry not enough milk!")
    if ini_cfe < n_cfe:
        sufficient = False
        print("Sorry not enough coffee")
    return sufficient


def coffee_function(init_water, init_coffee, init_milk, init_money):
    is_off = False
    while not is_off:
        user_select_coffee = input("  What would you like? (espresso/latte/cappuccino): ")
        if user_select_coffee == "off":
            is_off = True
        elif user_select_coffee == "report":
            machine_report(init_water, init_milk, init_coffee, init_money)
        else:
            (select_cfe_water, select_cfe_milk, select_cfe_coffee,
             select_cfe_cost) = user_coffee_details(user_select_coffee)
            is_every_thing_sufficient = is_sufficient(init_water, init_milk, init_coffee,
                                                      select_cfe_water, select_cfe_milk, select_cfe_coffee)
            if is_every_thing_sufficient:
                print("Please insert coins!")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                penny = int(input("How many pennies?: "))
                user_dollar = user_total_cost(quarters, dimes, nickles, penny)

                is_buy = can_buy(user_dollar, select_cfe_cost)
                final_decision(user_select_coffee, is_buy, user_dollar, select_cfe_cost)
                if is_buy:
                    init_water, init_milk, init_coffee, init_money = machine_update(select_cfe_water, select_cfe_milk,
                                                                                    select_cfe_coffee, select_cfe_cost,
                                                                                    init_water, init_milk, init_coffee,
                                                                                    init_money)


mh_water = 300
mh_milk = 200
mh_coffee = 100
mh_money = 0


coffee_function(mh_water, mh_milk, mh_coffee, mh_money)
