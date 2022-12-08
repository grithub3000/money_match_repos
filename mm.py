players = {}


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
        elif addition.capitalize() in players:
            print("Player not added. This name is already being used.")
        else:
            players.update({addition.capitalize(): 0})
    print(f"Player List: ", end="")
    for player in players.keys():
        print(f"{player}, ", end="")

def menu():
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
                                "\nPress ctrl 'z' to exit the program.\n>"))
        if action == "s":
            singles_results()
        elif action == "d":
            doubles_results()
        elif action == "add": 
            add_player()
        elif action == "totals": 
            totals()
        else:
            print("Invalid Input")

def totals():
    for player in players:
        print(f"{player}: ${players[player]}")

def singles_results():
    while True:
        winner = str(input("Which player won? Input 'b' to return to main menu"
            "\n>"))
        if winner == "b":
            menu()
        loser = str(input("Which player lost Input 'b' to return to main menu"
            "\n>"))
        if loser == "b":
            menu()
        if winner.capitalize() not in players.keys() or loser.capitalize() not in players.keys():
            print("One of the players you gave has not been added to the "
                "list. Please try again, or input 'b' to return to the "
                "main menu to add more players.")
        else:
            amount = int(input("How much money was this money match for?"
                "\n>$"))
            players[winner.capitalize()] += amount
            players[loser.capitalize()] -= amount
            break

def doubles_results():
    winning_team = []
    losing_team = []
    for i in range(2):
        while True:
            if i == 0:
                winner = input("Which team won (list one player at a time)? Input"
                    "'b' to return to the menu\n>")
            if i == 1:
                winner = input(">")
            if winner == 'b':
                menu()
            elif winner.capitalize() not in players:
                print("This player has not been added to the players list. "
                    "Please try again, or exit to the menu to add more "
                    "players.")
            else:
                winning_team.append(winner.capitalize())
                break
    for i in range(2):
        while True:
            if i == 0:
                loser = input("Which team lost (list one player at a time)? Input"
                    "'b' to return to the menu\n>")
            if i == 1:
                loser = input(">")
            if loser == 'b':
                menu()
            elif loser.capitalize() not in players:
                print("This player has not been added to the players list. "
                    "Please try again, or exit to the menu to add more "
                    "players.")
            else:
                losing_team.append(loser.capitalize())
                break
    amount = int(input("How much money was this money match for?\n>$"))
    for name in winning_team:
        players[name] += amount
    for name in losing_team:
        players[name] -= amount

def main():
    add_player()
    menu()
main()



