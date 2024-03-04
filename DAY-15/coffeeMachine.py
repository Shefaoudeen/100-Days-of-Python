import data

while 1:
    user_choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if user_choice == 'report':
        print(f"Water: {data.resources['water']}")
        print(f"Milk : {data.resources['milk']}")
        print(f"Coffee: {data.resources['coffee']}")
        print(f"Cash: {data.resources['cash']}")

    elif user_choice == 'latte' or user_choice == 'espresso' or user_choice == 'cappuccino':

        ingredients = True
        missing_ingredients = []

        for element in data.MENU[user_choice]['ingredients']:
            if data.resources[element] < data.MENU[user_choice]['ingredients'][element]:
                ingredients = False
                missing_ingredients.append(element)

        if ingredients:

            print("Please insert coins.")
            quarters = int(input("How many quarters? : "))
            dimes = int(input("How many dimes? : "))
            nickles = int(input("How many nickles? : "))
            pennies = int(input("How many pennies? : "))
            customer_cash = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

            if customer_cash >= data.MENU[user_choice]['cost']:

                data.resources['cash'] += data.MENU[user_choice]['cost']
                for element in data.MENU[user_choice]['ingredients']:
                    data.resources[element] -= data.MENU[user_choice]['ingredients'][element]
                remaining_cash = customer_cash - data.MENU[user_choice]['cost']

                if remaining_cash != 0:
                    print(f"Here is ${round(remaining_cash, 2)} in change")
                print(f"Here is your {user_choice} ☕ enjoy")

            else:
                print("Sorry that's not enough money. Money refund")

        else:
            print("Sorry there is not enough", end=" ")
            for element in missing_ingredients:
                print(element, end=" ")
            print("\n")
