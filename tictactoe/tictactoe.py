#-----------------------------------------------------------------------------------
def print_pole (pole):
    """
    Print pole 3х3
    """
    print("---------")
    for vertical_line in pole:
        print("|", " ".join(vertical_line), "|") # " " - space
    print("---------")
#-----------------------------------------------------------------------------------

def check_win(pole):
    """
    Check win: horisont_line, vertical_line or diagonal1 (2)
    """
    lines=[]
# horis line
    for row in pole:
        lines.append(row)
#vertical line
    for col in range(3):
        vertical_line = [pole[row][col] for row in range(3)]
        lines.append(vertical_line)
#diagonal
    diag1 = [pole[i][i] for i in range(3)] #left diagonal - i=i i=0 0.0 i=1 1.1 i=2 2.2
    diag2 = [pole[i][2-i] for i in range(3)]  # right diagonal 2-0=2,2-1=1,2-2=0
    lines.append(diag1)
    lines.append(diag2)
# ---------------------------------------
#count x 0
    count_x = sum(row.count("X") for row in pole)
    count_o = sum(row.count("0") for row in pole)
#---------------------------------------
#check imposible
    x_wins = ["X", "X", "X"] in lines
    o_wins = ["0", "0", "0"] in lines

# ^^^^ я побачив, що можно трохи оптимізувати нижчі іфи після одного з етапів
# але вже залишив як є, знову таки, щоб були видні різні стадії розробки

#------check win or draw
    if ["X", "X", "X"] in lines:
        return "X win!"
    if ["0", "0", "0"] in lines:
        return "0 win!"
    if any("_" in row for row in pole):  #
        return "Game not finished"
    if x_wins == o_wins: # impos
        return "Impossible"

    if abs(count_x - count_o) > 1: #impos
        return "Impossible"

#------in any other - draw

    return "Draw"
#-----------------------------------------------------------------------------------

def check_coordinate(coords, pole):
    """
    Chech user input coordinates
    """
    parts = coords.split() #//split coord

    if len(parts) != 2:
        print("You should enter two numbers!")
        return False

    if not all(part.isdigit() for part in parts):
        print("You should enter numbers!")
        return False

    x, y = map(int, parts) #//trans coord in int

    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return False

    if pole[x - 1][y - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False

    return True
#------------------------------------------------------------------
def step(pole, player):
    """
    user input sym and update the game pole.
    """
    while True:
        coords = input(f"Player {player}, enter coordinates (row and col with space from 1 to 3): ")
        if check_coordinate(coords, pole):  # check
            x, y = map(int, coords.split())

            pole[x - 1][y - 1] = player  # insert players syb on pole
            break

#---------------------------------------------------------------------------------
def main_f():
    """
       Main function to run Tic-Tac-Toe + menu
       """
    print("Welcome to Tic-Tac-Toe!")

    while True:
        # print menu
        print("\nMenu:")
        print("1. Play")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            # start
            pole = [["_"] * 3 for _ in range(3)]
            print_pole(pole)

            current_player = "X"
            while True:
                step(pole, current_player)
                print_pole(pole)

                result = check_win(pole)
                if result != "Game not finished":
                    print(result)
                    break

                # change player
                current_player = "0" if current_player == "X" else "X"

        elif choice == "2":
            # bb user
            print("Thanks for playing Tic-Tac-Toe! Goodbye!")
            break

        else:
            # incorect
            print("Invalid choice. Please enter 1 or 2.")

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main_f()
