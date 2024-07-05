import random

name = None

def greet_user(name):
    greetings = [f"Welcome {name}", "Welcome buddy!", "Howdy!"]
    greeting_index = random.randint(0, len(greetings) - 1)
    print(greetings[greeting_index])

starting = True

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

def show_user_menu():
    print("1. Continue")
    print("2. Exit")
    print("3. Bagpack")
    print("4. Pocket monsters")
    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Continue")
    elif choice == 2:
        print("Exit")
    elif choice == 3:
        print("Bagpack")
    elif choice == 4:
        print("Pokemons")
    else:
        print("Invalid option. Please choose again.")

def start_new_game():
    regions = {
        "Kanto": ["Bulbasaur", "Charmander", "Squirtle"],
        "Johto": ["Chikorita", "Cyndaquil", "Totodile"],
        "Hoenn": ["Treecko", "Torchic", "Mudkip"],
        "Sinnoh": ["Turtwig", "Chimchar", "Piplup"],
        "Unova": ["Snivy", "Tepig", "Oshawott"],
        "Kalos": ["Chespin", "Fennekin", "Froakie"],
        "Alola": ["Rowlet", "Litten", "Popplio"],
        "Galar": ["Grookey", "Scorbunny", "Sobble"],
        "Paldea": ["Sprigatito", "Fuecoco", "Quaxly"]
    }

    selected_region = random.choice(list(regions.keys()))
    starters = regions[selected_region]
    print(f"For starting, please choose a pocket monster for your region: {selected_region}")
    for i, starter in enumerate(starters, 1):
        print(f"{i}. {starter}")
    
    choice = int(input("Choose your starter Pokémon: "))
    if 1 <= choice <= len(starters):
        selected_pokemon = starters[choice - 1]
        print(f"You have chosen {selected_pokemon}!")
        print(f"{selected_pokemon} has been added to your pokedex! Froakie is in your team now! :D")
        print("===========STATS===========")
        print("Level: 5\nHP: 20\nAttack: 10\nDefense: 10\nSpeed: 10\nSpecial Attack: 10\nSpecial Defense: 10\nMoves: Tackle, Growl")

    else:
        print("Invalid choice. Please try again.")

def leaderboard():
    print("Leaderboard is currently empty.")

def main_menu():
    while True:
        if starting:
            display_help()
            print("Welcome to the Pokémon game!")
            starting = False
        else:
            show_user_menu()    
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            print("Loading game...")
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
