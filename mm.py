players = []


def add_player():
    while True:
        count = len(players)
        print("\n")
        addition = str(input("Input each player's name. When finished, input"
                    " 'DONE':\n>"))
        if addition == "DONE":
            break
        elif len(addition) < 3:
            print("Name not added. Each player name must be at least 3 characters.")
        else:
            players.append([addition])
            players[count].append(0)
    print(f"Player List: {players}")

def totals():
    for i in range(len(players)):
        print(f"{players[i][0]}: ${players[i][1]}")

def singles_results():
    while True:
        w1 = str(input("Which player won? Input b to return to main menu\n>"))
        l1 = str(input("Which player lost Input b to return to main menu?\n>"))

        if not any(w1 in sublist for sublist in players) or not any (l1 in sublist for sublist in players):
            print("One of the players you gave has not been added to the "
                "list. Please try again, or input 'b' to return to the "
                "main menu to add more players.")



def main():

    add_player()

    while True:
        if len(players) < 2:
            print("\nYou must have 2 or more players to play. Please add at least",
                    (2 - len(players)), "more")
            add_player()
        else:
            break

    while True:
        print("\n")
        action = str(input("Input one of the following:\n" 
                                "'s', or 'd' to report match results (for singles "
                                "or doubles)."
                                "\n'add' to add more players."
                                "\n'totals' to display the money counts."
                                "\n'QUIT' to exit the program.\n>"))
        if action == "s":
            singles_results()
        elif action == "d":
            doubles_results()
        elif action == "add": 
            add_player()
        elif action == "totals": 
            totals()
        elif action == "QUIT":
            final = str(input("Are you sure? All data will be lost." 
                    "Input YES/NO:\n>"))
            if final == "YES": 
                break
        else:
            print("Invalid Input")

main()



