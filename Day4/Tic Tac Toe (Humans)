board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
def print_board():
    for row in board:
        print(" | ".join(row))
    print()
def check_winner(player):

    # rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False
def check_draw():
    for row in board:
        if "_" in row:
            return False
    return True
current_player = "X"
while True:

    print_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))

    if board[row][col] != "_":
        print("Invalid move")
        continue

    board[row][col] = current_player

    if check_winner(current_player):
        print_board()
        print(current_player, "wins!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

########                OUTPUT                ########
_ | _ | _
_ | _ | _
_ | _ | _

Enter row (0-2):  0
Enter col (0-2):  0
X | _ | _
_ | _ | _
_ | _ | _

Enter row (0-2):  0
Enter col (0-2):  1
X | O | _
_ | _ | _
_ | _ | _

Enter row (0-2):  1
Enter col (0-2):  1
X | O | _
_ | X | _
_ | _ | _

Enter row (0-2):  0
Enter col (0-2):  2
X | O | O
_ | X | _
_ | _ | _

Enter row (0-2):  2
Enter col (0-2):  2
X | O | O
_ | X | _
_ | _ | X

X wins!
