def game_menu():
    print("Press 1 To Start Game")
    print("Press 2 To Select Difficulty")
    print("Press 3 To View Rules")

    menu_selection = False
    while not menu_selection:
        selection = input("What would you like to do?\n")
        if selection == 1:
            menu_selection = True

        elif selection == 2:
            menu_selection = True

        elif selection == 3:
            menu_selection = True

        else:
            print("Select 1, 2 or 3")
