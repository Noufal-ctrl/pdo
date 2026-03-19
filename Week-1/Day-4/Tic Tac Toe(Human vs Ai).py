import math
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
human = "X"
ai = "O"
def print_board():
    for row in board:
        print(" | ".join(row))
    print()
def check_winner(player):

    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True


    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True


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
def minimax(is_maximizing):

    if check_winner(ai):
        return 1

    if check_winner(human):
        return -1

    if check_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":
                    board[i][j] = ai

                    score = minimax(False)

                    board[i][j] = "_"

                    best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":
                    board[i][j] = human

                    score = minimax(True)

                    board[i][j] = "_"

                    best_score = min(score, best_score)

        return best_score
def ai_move():

    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):

            if board[i][j] == "_":

                board[i][j] = ai
                score = minimax(False)
                board[i][j] = "_"

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = ai
while True:

    print_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != "_":
        print("Invalid move")
        continue

    board[row][col] = human

    if check_winner(human):
        print_board()
        print("You win!")
        break

    if check_draw():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner(ai):
        print_board()
        print("AI wins!")
        break

    if check_draw():
        print_board()
        print("Draw!")
        break

########                OUTPUT                ########
_ | _ | _
_ | _ | _
_ | _ | _

Enter row (0-2):  1
Enter column (0-2):  1
O | _ | _
_ | X | _
_ | _ | _

Enter row (0-2):  2
Enter column (0-2):  2
O | _ | O
_ | X | _
_ | _ | X

Enter row (0-2):  0
Enter column (0-2):  1
O | X | O
_ | X | _
_ | O | X

Enter row (0-2):  2
Enter column (0-2):  1
Invalid move
O | X | O
_ | X | _
_ | O | X

Enter row (0-2):  2
Enter column (0-2):  0
O | X | O
O | X | _
X | O | X

Enter row (0-2):  1
Enter column (0-2):  2
O | X | O
O | X | X
X | O | X

Draw!
