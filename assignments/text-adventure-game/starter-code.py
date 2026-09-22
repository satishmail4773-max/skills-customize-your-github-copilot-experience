def start_game():
    inventory = []
    print("Welcome to the Forest of Echoes!")
    print("You are standing at a crossroads. A mysterious path leads north.")
    print("Type 'north' to continue or 'quit' to leave the game.")

    choice = input("What do you do? ").lower()

    if choice == "north":
        print("You follow the path and find a glowing lantern.")
        inventory.append("lantern")
        print("You picked up a lantern.")
    elif choice == "quit":
        print("You leave the forest and the adventure ends.")
        return
    else:
        print("That choice is not recognized. The forest remains quiet.")

    print("Your inventory:", inventory)
    print("The adventure continues...")


start_game()
