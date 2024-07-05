import random

name = None
pokemon_team = []
bag = []
pokedex = {}
locations = ["Forest", "Mountain", "Lake", "Desert", "Cave", "Field"]

def greet_user(name):
    greetings = [f"Welcome {name}", "Welcome buddy!", "Howdy!"]
    greeting_index = random.randint(0, len(greetings) - 1)
    print(greetings[greeting_index])

def display_help():
    print("Options:")
    print("1. Continue")
    print("2. Start New")
    print("3. Leaderboard")
    print("4. Exit")

def ask_user_name():
    global name
    print('Hello there! What is your name?')
    name = str(input("Your name: "))
    greet_user(name)

def show_main_menu():
    print("Main Menu Options:")
    print("1. Continue")
    print("2. Exit")
    print("3. Bagpack")
    print("4. Pocket monsters")
    print("5. Show all Pokémons")
    print("6. Check Pokémon by number")
    print("7. See Pokémon stats")
    print("8. View Pokémon moves")
    print("9. Travel")

def show_pokemon_menu():
    print("Options:")
    print("1. Stats")
    print("2. Moves")
    print("3. Feed")
    print("4. Fight")
    print("0. Back to Main Menu")

def start_new_game():
    global pokemon_team, pokedex
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
        pokemon_stats = {
            'name': selected_pokemon,
            'level': 5,
            'hp': 20,
            'attack': 10,
            'defense': 10,
            'speed': 10,
            'special_attack': 10,
            'special_defense': 10,
            'moves': ['Tackle', 'Growl']
        }
        pokemon_team.append(pokemon_stats)
        pokedex[selected_pokemon] = {
            'number': len(pokedex) + 1,
            'stats': pokemon_stats
        }
        print(f"{selected_pokemon} has been added to your pokedex! {selected_pokemon} is in your team now! :D")
        print("===========STATS===========")
        print(f"Level: 5\nHP: 20\nAttack: 10\nDefense: 10\nSpeed: 10\nSpecial Attack: 10\nSpecial Defense: 10\nMoves: Tackle, Growl")
    else:
        print("Invalid choice. Please try again.")

def leaderboard():
    print("Leaderboard is currently empty.")

def show_all_pokemons():
    if not pokemon_team:
        print("You have no Pokémon in your team.")
    else:
        print("All captured Pokémons:")
        for idx, pokemon in enumerate(pokemon_team, 1):
            print(f"{idx}. {pokemon['name']}")

def check_pokemon_by_number():
    number = int(input("Enter Pokémon number: "))
    for pokemon in pokedex.values():
        if pokemon['number'] == number:
            print(f"{pokemon['name']}: {pokemon['stats']}")
            return
    print("No Pokémon found with that number.")

def see_pokemon_stats(name=None):
    if not name:
        name = input("Enter Pokémon name: ")
    for pokemon in pokemon_team:
        if pokemon['name'].lower() == name.lower():
            print(f"Stats for {pokemon['name']}:")
            print(f"Level: {pokemon['level']}\nHP: {pokemon['hp']}\nAttack: {pokemon['attack']}\nDefense: {pokemon['defense']}\nSpeed: {pokemon['speed']}\nSpecial Attack: {pokemon['special_attack']}\nSpecial Defense: {pokemon['special_defense']}")
            return
    print("No Pokémon found with that name.")

def view_pokemon_moves(name=None):
    if not name:
        name = input("Enter Pokémon name: ")
    for pokemon in pokemon_team:
        if pokemon['name'].lower() == name.lower():
            print(f"Moves for {pokemon['name']}: {', '.join(pokemon['moves'])}")
            return
    print("No Pokémon found with that name.")

def travel():
    location = random.choice(locations)
    print(f"Traveling to {location}...")
    encounter = random.randint(1, 100)
    if encounter > 50:
        random_pokemon = random.choice(list(pokedex.keys()))
        print(f"You encountered a wild {random_pokemon}!")
        catch_pokemon(random_pokemon)
    else:
        print("No Pokémon encountered.")

def catch_pokemon(pokemon_name):
    global pokedex
    print(f"Attempting to catch {pokemon_name}...")
    catch_chance = random.randint(1, 100)
    if catch_chance > 50:
        new_pokemon_stats = {
            'name': pokemon_name,
            'level': random.randint(1, 5),
            'hp': random.randint(10, 30),
            'attack': random.randint(5, 15),
            'defense': random.randint(5, 15),
            'speed': random.randint(5, 15),
            'special_attack': random.randint(5, 15),
            'special_defense': random.randint(5, 15),
            'moves': ['Tackle', 'Growl']
        }
        pokemon_team.append(new_pokemon_stats)
        pokedex[pokemon_name] = {
            'number': len(pokedex) + 1,
            'stats': new_pokemon_stats
        }
        print(f"Congratulations! You caught {pokemon_name}!")
    else:
        print(f"{pokemon_name} escaped!")

def main_menu():
    global starting
    ask_user_name()
    start_new_game()
    while True:
        show_main_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            print("Continuing game...")
        elif choice == 2:
            print("Exiting the game. Goodbye!")
            break
        elif choice == 3:
            print("Bagpack is currently empty.")
        elif choice == 4:
            show_all_pokemons()
            while True:
                sub_choice = int(input("Choose a Pokémon to view details or 0 to go back: "))
                if sub_choice == 0:
                    break
                elif 1 <= sub_choice <= len(pokemon_team):
                    pokemon = pokemon_team[sub_choice - 1]
                    print(f"Selected Pokémon: {pokemon['name']}")
                    while True:
                        show_pokemon_menu()
                        detail_choice = int(input("Choose an option: "))
                        if detail_choice == 0:
                            break
                        elif detail_choice == 1:
                            see_pokemon_stats(pokemon['name'])
                        elif detail_choice == 2:
                            view_pokemon_moves(pokemon['name'])
                        elif detail_choice == 3:
                            print(f"Feeding {pokemon['name']}...")
                            pokemon['hp'] += 5
                            print(f"{pokemon['name']} gained 5 HP. Current HP: {pokemon['hp']}")
                        elif detail_choice == 4:
                            print(f"Initiating a fight for {pokemon['name']}...")
                            # Implement fight logic here
                        else:
                            print("Invalid option. Please choose again.")
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 5:
            show_all_pokemons()
        elif choice == 6:
            check_pokemon_by_number()
        elif choice == 7:
            see_pokemon_stats()
        elif choice == 8:
            view_pokemon_moves()
        elif choice == 9:
            travel()
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main_menu()
