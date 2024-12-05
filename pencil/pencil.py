import random
#----------------------------------------------------------
def draw_pencils(pencils):
    """
    Print pencils
    """
    print("|" * pencils) # print pencils

#----------------------------------------------------------
def get_pencils():
    """
    Enter start quantity pencil, return int pencil
    """
    while True:
        pencils = input("How many pencils would you like to use: ")
        if not pencils.isdigit() and int(pencils) <= 0:
            print("The number of pencils should be numeric and >0")

        else:
            return int(pencils)

#----------------------------------------------------------
def choice_first_player(player1, player2):
    """
    Choice who starting game
    """
    while True:
        first_player = input(f"Who will be the first ({player1}, {player2}): ")
        if first_player not in {player1, player2}:
            print(f"Choose between '{player1}' and '{player2}'")
        else:
            return first_player
#----------------------------------------------------------

def human(max_pencils):
    """
    Human move, return how manu pencils human took
    """
    while True:
        print("Enter how many pancil you take (1, 2 or 3) >")
        move = input()

        if move not in {"1", "2", "3"}:
            print("Possible values: '1', '2' or '3'")
        elif int(move) > max_pencils:
            print("Too many pencils take")
        else:
            return int(move)
#----------------------------------------------------------

def bot_move(pencils):
    """
    bot move +  return
    """
    if pencils % 4 == 0: # bot take 3
        return 3

    elif pencils % 4 == 3: # bot take 2
        return 2

    elif pencils % 2 == 1: # bot take 1
        return 1

    else:
        return random.randint (1, min (3, pencils))
#----------------------------------------------------------

def play_game():
    """
    game logic
    """
    # Pl name
    player1 = "John"
    player2 = "Jack"
    pencils = get_pencils()
    first_player = choice_first_player(player1, player2) #
    draw_pencils(pencils)

    current_player = first_player

    while pencils > 0:
        print(f"{current_player}'s turn!")
        if current_player == player1:
            move = human(pencils)
        else:
            move = bot_move(pencils)
            print(move)  # bot move
        pencils -= move
        if pencils > 0:
            draw_pencils(pencils)
        current_player = player1 if current_player == player2 else player2
#
    print(f"{current_player} won!")
#----------------------------------------------------------

def menu():
    """
    Main menu
    """
    while True:
        print("Menu")
        print("1. Start game")
        print("2. Exit")
        choice = input("You choice: > ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Thx! Bb. See you latter")
            break
        else:
            print("Incorrect. Try again ")
#----------------------------------------------------------

if __name__ == "__main__":
    menu()

