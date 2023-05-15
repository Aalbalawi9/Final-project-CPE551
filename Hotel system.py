from datetime import datetime


SINGLE_PRICE = 50
DOUBLE_PRICE = 80
DELUXE_PRICE = 150


HOT_DRINK_PRICE = 2
COLD_DRINK_PRICE = 2.5
BREAKFAST_PRICE = 5
LUNCH_PRICE = 10
DINNER_PRICE = 15


SHORTS_PRICE = 3
SHIRT_PRICE = 2
PANTS_PRICE = 4
DRESS_PRICE = 5


BOWLING_PRICE = 8
CHESS_PRICE = 2
PC_PRICE = 6


room_prices = {
    1: {"type": "Single", "price": SINGLE_PRICE},
    2: {"type": "Double", "price": DOUBLE_PRICE},
    3: {"type": "Deluxe", "price": DELUXE_PRICE}
}


menu_prices = {
    1: {"name": "Hot Drink", "price": HOT_DRINK_PRICE},
    2: {"name": "Cold Drink", "price": COLD_DRINK_PRICE},
    3: {"name": "Breakfast", "price": BREAKFAST_PRICE},
    4: {"name": "Lunch", "price": LUNCH_PRICE},
    5: {"name": "Dinner", "price": DINNER_PRICE},
    6: {"name": "Nothing", "price": 0}
}


laundry_prices = {
    1: {"name": "Shorts", "price": SHORTS_PRICE},
    2: {"name": "Shirt", "price": SHIRT_PRICE},
    3: {"name": "Pants", "price": PANTS_PRICE},
    4: {"name": "Dress", "price": DRESS_PRICE},
    5: {"name": "Nothing", "price": 0}
}


game_prices = {
    1: {"name": "Bowling", "price": BOWLING_PRICE},
    2: {"name": "Chess", "price": CHESS_PRICE},
    3: {"name": "PC", "price": PC_PRICE},
    4: {"name": "Nothing", "price": 0}
}


guest_info = {
    "name": "",
    "email": "",
    "phone": "",
    "checkin_date": "",
    "checkout_date": "",
    "room_type": 0,
    "menu_items": [],
    "laundry_items": [],
    "game_items": []
}

def display_menu(menu_dict):
    for key, item in menu_dict.items():
        print(f"{key}. {item['name']} - ${item['price']}")

def calculate_cost(item_list, price_dict):
    return sum([price_dict[item]['price'] for item in item_list])


print("Welcome to Albalawi hotel")
while True:
    print("\nPlease select an option:")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Exit")

    option = int(input("Enter your choice (1-3): "))

    if option == 1:

        guest_info["name"] = input("Please enter your name: ")
        guest_info["email"] = input("Please enter your email: ")
        guest_info["phone"] = input("Please enter your phone number: ")
        guest_info["checkin_date"] = input("Please enter your check-in date (DD/MM/YYYY): ")
        guest_info["checkout_date"] = input("Please enter your check-out date (DD/MM/YYYY): ")


        print("\nHere are the available room types and prices:")
        for room_num, room_info in room_prices.items():
            print(f"{room_num}. Room {room_num}: {room_info['type']} - ${room_info['price']} per night")


        guest_info["room_type"] = int(input("\nPlease select a room type (1-3): "))


        print("\nHere's our hotel restaurant menu:")
        display_menu(menu_prices)


        menu_items = input("\nPlease enter the numbers of the menu items you want (e.g. '1 3 4'): ")
        guest_info["menu_items"] = list(map(int, menu_items.split()))


        print("\nHere's our laundry list:")
        display_menu(laundry_prices)


        laundry_items = input("\nPlease enter the numbers of the laundry items you want (e.g. '1 2 4'): ")
        guest_info["laundry_items"] = list(map(int, laundry_items.split()))


        print("\nHere's our game list:")
        display_menu(game_prices)


        game_items = input("\nPlease enter the numbers of the game items you want (e.g. '1 3'): ")
        guest_info["game_items"] = list(map(int, game_items.split()))


        room_cost = room_prices[guest_info["room_type"]]["price"] * (
                    datetime.strptime(guest_info["checkout_date"], "%d/%m/%Y") - datetime.strptime(
                guest_info["checkin_date"], "%d/%m/%Y")).days


        menu_cost = calculate_cost(guest_info["menu_items"], menu_prices)
        laundry_cost = calculate_cost(guest_info["laundry_items"], laundry_prices)
        game_cost = calculate_cost(guest_info["game_items"], game_prices)


        total_cost = room_cost + menu_cost + laundry_cost + game_cost


        print("\nThank you for your reservation, " + guest_info["name"] + "!")
        print("Here's your booking information:")
        print("Room type: " + room_prices[guest_info["room_type"]]["type"])
        print("Check-in date: " + guest_info["checkin_date"])
        print("Check-out date: " + guest_info["checkout_date"])
        print("Total cost for room reservation: $" + str(room_cost))
        print("Menu items: " + ", ".join([menu_prices[item]["name"] for item in guest_info["menu_items"]]))
        print("Total cost for menu items: $" + str(menu_cost))
        print("Laundry items: " + ", ".join([laundry_prices[item]["name"] for item in guest_info["laundry_items"]]))
        print("Total cost for laundry: $" + str(laundry_cost))
        print("Game items: " + ", ".join([game_prices[item]["name"] for item in guest_info["game_items"]]))
        print("Total cost for games: $" + str(game_cost))
        print("Total cost: $" + str(total_cost))

    elif option == 2:

        room_num = int(input("Please enter your room number: "))


        room_type = room_prices[guest_info["room_type"]]["type"]
        checkin_date = guest_info["checkin_date"]
        checkout_date = guest_info["checkout_date"]
        room_cost = room_prices[guest_info["room_type"]]["price"] * (
                    datetime.strptime(checkout_date, "%d/%m/%Y") - datetime.strptime(checkin_date, "%d/%m/%Y")).days
        menu_items = [menu_prices[item]["name"] for item in guest_info["menu_items"]]
        menu_cost = calculate_cost(guest_info["menu_items"], menu_prices)
        laundry_items = [laundry_prices[item]["name"] for item in guest_info["laundry_items"]]
        laundry_cost = calculate_cost(guest_info["laundry_items"], laundry_prices)
        game_items = [game_prices[item]["name"] for item in guest_info["game_items"]]
        game_cost = calculate_cost(guest_info["game_items"], game_prices)
        total_cost = room_cost + menu_cost + laundry_cost + game_cost


        print("\nGuest Information:")
        print("Name: " + guest_info["name"])
        print("Email: " + guest_info["email"])
        print("Phone: " + guest_info["phone"])
        print("Room Type: " + room_type)
        print("Check-in Date: " + checkin_date)
        print("Check-out Date: " + checkout_date)
        print("Total Bill: $" + str(total_cost))

    elif option == 3:
        print("Thank you for Visiting Albalawi hotel !")
        break

    else:
        print("Invalid option. Please select a valid option (1-3).")


