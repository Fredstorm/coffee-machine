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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
enough_water = True
enough_milk = True
enough_coffee = True

five_cent = 0
ten_cent = 0
twenty_cent = 0
fifty_cent = 0
dollar_coin = 0
two_dollar_coin = 0
payment = 0
change = 0

end = False

while end is False:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        end = True
    elif choice == "report":
        print(resources)

    if choice == "espresso":
        if int(resources.get("water")) >= 50:
            enough_water = True
        else:
            print("Sorry there is not enough water.")
            enough_water = False
        if int(resources.get("coffee")) >= 18:
            enough_coffee = True
        else:
            print("Sorry there is not enough coffee.")
            enough_coffee = False
        if enough_water == True and enough_coffee == True:
            print("Please insert coins.")
            five_cent = int(input("How many five cent coins?"))
            ten_cent = int(input("How many ten cent coins?"))
            twenty_cent = int(input("How many twenty cent coins?"))
            fifty_cent = int(input("How many fifty cent coins?"))
            dollar_coin = int(input("How many one dollar coins?"))
            two_dollar_coin = int(input("How many two dollar coins?"))
            payment = five_cent * 0.05 + ten_cent * 0.1 + twenty_cent * 0.2 + fifty_cent * 0.5 + dollar_coin + two_dollar_coin * 2
            if payment >= float(MENU[choice].get("cost")):
                change = payment - float(MENU[choice].get("cost"))
                print(f"Here is ${change} in change")
                print(f"Here is your {choice} ☕")
                resources["water"] -= 50
                resources["coffee"] -= 18
    if choice == "latte":
        if int(resources.get("water")) >= 200:
            enough_water = True
        else:
            print("Sorry there is not enough water.")
            enough_water = False
        if int(resources.get("milk")) >= 150:
            enough_milk = True
        else:
            print("Sorry there is not enough milk.")
            enough_milk = False
        if int(resources.get("coffee")) >= 24:
            enough_coffee = True
        else:
            print("Sorry there is not enough coffee.")
            enough_coffee = False
        if enough_water == True and enough_milk == True and enough_coffee == True:
            print("Please insert coins.")
            five_cent = int(input("How many five cent coins?"))
            ten_cent = int(input("How many ten cent coins?"))
            twenty_cent = int(input("How many twenty cent coins?"))
            fifty_cent = int(input("How many fifty cent coins?"))
            dollar_coin = int(input("How many one dollar coins?"))
            two_dollar_coin = int(input("How many two dollar coins?"))
            payment = five_cent * 0.05 + ten_cent * 0.1 + twenty_cent * 0.2 + fifty_cent * 0.5 + dollar_coin + two_dollar_coin * 2
            if payment >= float(MENU[choice].get("cost")):
                change = payment - float(MENU[choice].get("cost"))
                print(f"Here is ${change} in change")
                print(f"Here is your {choice} ☕")
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
    if choice == "cappuccino":
        if int(resources.get("water")) >= 250:
            enough_water = True
        else:
            print("Sorry there is not enough water.")
            enough_water = False
        if int(resources.get("milk")) >= 100:
            enough_milk = True
        else:
            print("Sorry there is not enough milk.")
            enough_milk = False
        if int(resources.get("coffee")) >= 24:
            enough_coffee = True
        else:
            print("Sorry there is not enough coffee.")
            enough_coffe = False
        if enough_water == True and enough_milk == True and enough_coffee == True:
            print("Please insert coins.")
            five_cent = int(input("How many five cent coins?"))
            ten_cent = int(input("How many ten cent coins?"))
            twenty_cent = int(input("How many twenty cent coins?"))
            fifty_cent = int(input("How many fifty cent coins?"))
            dollar_coin = int(input("How many one dollar coins?"))
            two_dollar_coin = int(input("How many two dollar coins?"))
            payment = five_cent * 0.05 + ten_cent * 0.1 + twenty_cent * 0.2 + fifty_cent * 0.5 + dollar_coin + two_dollar_coin * 2
            if payment >= float(MENU[choice].get("cost")):
                change = payment - float(MENU[choice].get("cost"))
                print(f"Here is ${change} in change")
                print(f"Here is your {choice} ☕")
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100