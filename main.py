import random

# IT IS HARD ON PHONE, TERRIBLY SORRY FOR LESS ADDITIONS


name = None

def greet_user(name):
    greetings = [f"Welcome {name}", "Welcome buddy!", "Howdy man!"]
    length = len(greetings)
    greeting_index = random.randint(0, length - 1)
    print(greetings[greeting_index])

def display_help():
    print("Options:")
    print("1. Load")
    print("2. Start New")
    print("3. Leaderboard")
    print("4. Exit")

def ask_user_name():
    global name
    print('Hello there! What is your name?')
    name = str(input("Your name: "))
    greet_user(name)

def start_new_game():
    areas = ["Forest", "Desert", "Mountain"]
    vehicles = ["Car", "Bike", "Horse"]

    print("Select an area to go to:")
    for i, area in enumerate(areas, 1):
        print(f"{i}. {area}")
    
    
    area_choice = int(input("Your choice: "))
    if not type(area_choice) is string:
      print('Please input only the numbers')
      start_new_game()
    
    selected_area = areas[area_choice - 1]

    print("Select a vehicle to use:")
    for i, vehicle in enumerate(vehicles, 1):
        print(f"{i}. {vehicle}")

    vehicle_choice = int(input("Your choice: "))
    selected_vehicle = vehicles[vehicle_choice - 1]

    print(f"You are heading to the {selected_area} with your {selected_vehicle}!")

def leaderboard():
    print("Leaderboard is currently empty.")

def main_menu():
    while True:
        display_help()
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            print("Loading game...")
            # TODO:Add logic to load game
        elif choice == "2":
            start_new_game()
        elif choice == "3":
            leaderboard()
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    ask_user_name()
    main_menu()
