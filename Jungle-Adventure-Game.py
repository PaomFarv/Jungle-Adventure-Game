first_input = input("Do you want to play this game (Yes/No)? ").lower().strip()
if first_input == "yes":
    print("Imagine you are in a jungle.")
    second = input("Do you want to explore it (yes/no)? ").strip().lower()
    if second == "yes":
        print("You have three routes to go through.")
        third = input("You have to pick one (1, 2, or 3): ").strip()
        if third == "1":
            print("Oh no! You encountered a tiger and it attacked you. Game over!")
        elif third == "2":
            print("Oops! You fell into a big hole and couldn't escape. Game over!")
        elif third == "3":
            print("Good choice! But now you are lost in this big jungle.")
            fourth = input("Do you want to keep going? (yes/no): ").strip().lower()
            if fourth == "yes":
                print("You found a way out of the jungle! Congratulations! (GAME OVER!)")
            elif fourth == "no":
                print("You decided to stay put, but unfortunately, no help arrived. Game over!")
            else:
                print("Invalid input. Game over!")
        else:
            print("Invalid route selection. Game over!")
    elif second == "no":
        print("You chose not to explore the jungle. Game over!")
    else:
        print("Invalid input. Game over!")
elif first_input == "no":
    print("You chose not to play. Goodbye!")
else:
    print("Invalid input. Please restart the game.")
