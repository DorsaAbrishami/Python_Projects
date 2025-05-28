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

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

machine_status = True

def report():
    global water, milk, coffee,money
    print(f'Water:  {water} ML')
    print(f'Milk:   {milk} ML')
    print(f'Coffee: {coffee} ML')
    print(f'Money:  {money} ML')

def espresso():
    global water, coffee
    if water < MENU["espresso"]['ingredients']['water']:
        print(f"Sorry there is not enough water {water}")
    elif coffee < MENU["espresso"]['ingredients']['coffee']:
        print(f"Sorry there is not enough coffee {coffee}")
    else:
        print("Please insert coin")
        quarters = int(input("How many quarters?"))
        dimes    = int(input("How many dimes?"))
        nickles  = int(input("How many nickles?"))
        pennies  = int(input("How many pennies?"))
        sum = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
        if sum > MENU["espresso"]["cost"]:
            change = sum - MENU["espresso"]["cost"]
            print(f'Here is $ {round(change,2)}.')
            print("Here is your espresso!")
            water = water - MENU["espresso"]['ingredients']['water']
            coffee = coffee - MENU["espresso"]['ingredients']['coffee']
        else:
            print("Sorry there is not enough money")
def latte():
    global water,milk, coffee
    if water < MENU["latte"]['ingredients']['water']:
        print(f"sorry there is not enough water {water}")
    elif milk < MENU["latte"]['ingredients']['milk']:
        print(f"sorry there is not enough milk {milk} ")
    elif coffee < MENU["latte"]['ingredients']['coffee']:
        print(f"sorry there is not enough coffee {coffee}")
    else:
        print("please insert coins")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        sum = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        if sum > MENU["latte"]["cost"]:
            change = sum - MENU["latte"]["cost"]
            print(f'Here is $ {round(change, 2)}.')
            print("Here is your latte!")
            water = water - MENU["latte"]['ingredients']['water']
            milk = milk - MENU["latte"]["ingredients"]["milk"]
            coffee = coffee - MENU["espresso"]['ingredients']['coffee']
        else:
            print("sorry not enough money!")

def cappuccino():
    global water, milk, coffee
    if water < MENU["cappuccino"]["ingredients"]["water"]:
        print(f"sorry there is not enough water {water}")
    elif milk < MENU["cappuccino"]['ingredients']['milk']:
        print(f"sorry there is not enough milk {milk} ")
    elif coffee < MENU["cappuccino"]['ingredients']['coffee']:
        print(f"sorry there is not enough coffee {coffee}")
    else:
        print("please insert coins")
        quarters = int(input("How many quarters?"))
        # quarters = int(input("please insert coins" /n "How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        sum = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        if sum > MENU["cappuccino"]["cost"]:
            change = round(sum - MENU["cappuccino"]["cost"], 2)
            print(f"here is your change ${change}")
            print("here is your cappuccino!")
            water = water - MENU["cappuccino"]["ingredients"]["water"]
            milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
            coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]
        else:
            print("sorry there is not enough money!")



while machine_status == True:
    order = input("What would you like? (Espresso/Latte/Cappuccino/):").lower()
    if order == "report":
        report()
    elif order == "espresso":
        espresso()
        continue
    elif order == "latte":
        latte()
        continue
    elif order == "cappuccino":
        cappuccino()
        continue
    elif order == "off":
        machine_status = False