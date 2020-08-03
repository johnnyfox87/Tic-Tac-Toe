mat = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def show_state():
    sep = "---------"
    print(sep)
    print("|", mat[0][0], mat[0][1], mat[0][2], "|")
    print("|", mat[1][0], mat[1][1], mat[1][2], "|")
    print("|", mat[2][0], mat[2][1], mat[2][2], "|")
    print(sep)


def get_row_result(row) -> str:
    if mat[row][0] == "X" and mat[row][1] == "X" and mat[row][2] == "X":
        return "X"
    if mat[row][0] == "O" and mat[row][1] == "O" and mat[row][2] == "O":
        return "O"
    if mat[row][0] == "_" or mat[row][1] == "_" or mat[row][2] == "_":
        return "_"
    return "F"


def get_col_result(col) -> str:
    if mat[0][col] == "X" and mat[1][col] == "X" and mat[2][col] == "X":
        return "X"
    if mat[0][col] == "O" and mat[1][col] == "O" and mat[2][col] == "O":
        return "O"
    if mat[0][col] == "_" or mat[1][col] == "_" or mat[2][col] == "_":
        return "_"
    return "F"


def get_cross1_result() -> str:
    if mat[0][0] == "X" and mat[1][1] == "X" and mat[2][2] == "X":
        return "X"
    if mat[0][0] == "O" and mat[1][1] == "O" and mat[2][2] == "O":
        return "O"
    if mat[0][0] == "_" or mat[1][1] == "_" or mat[2][2] == "_":
        return "_"
    return "F"


def check_count() -> bool:
    x_count = mat[0].count("X") + mat[1].count("X") + mat[2].count("X")
    o_count = mat[0].count("O") + mat[1].count("O") + mat[2].count("O")
    if -2 < x_count - o_count < 2:
        return True
    return False


def get_cross2_result() -> str:
    if mat[2][0] == "X" and mat[1][1] == "X" and mat[0][2] == "X":
        return "X"
    if mat[2][0] == "O" and mat[1][1] == "O" and mat[0][2] == "O":
        return "O"
    if mat[2][0] == "_" or mat[1][1] == "_" or mat[0][2] == "_":
        return "_"
    return "F"


def check_winner() -> bool:
    result = [get_row_result(0), get_row_result(1), get_row_result(2), get_col_result(0), get_col_result(1),
              get_col_result(2), get_cross1_result(), get_cross2_result()]
    if check_count():
        if result.count("X") == 1 and result.count("O") == 0:
            print("X wins")
        elif result.count("O") == 1 and result.count("X") == 0:
            print("O wins")
        elif result.count("X") >= 1 and result.count("O") >= 1:
            print("Impossible")
        elif result.__contains__("_"):
            print("Game not finished")
            return False
        else:
            print("Draw")
    else:
        print("Impossible")
    return True


def check_input(player):
    ack = False
    while not ack:
        user_input = input("Enter the coordinates player " + player + ":").split()
        if len(user_input) != 2:
            print("You should enter numbers!")
            continue
        if not user_input[0].isdigit() or not user_input[1].isdigit():
            print("You should enter numbers!")  # if the user enters other symbols;
            continue
        user_move = [int(user_input[0]), int(user_input[1])]
        if not (1 <= user_move[0] <= 3 and 1 <= user_move[1] <= 3):
            print("Coordinates should be from 1 to 3!")  # if the user goes beyond the field.
            continue
        move = [3 - user_move[1], user_move[0] - 1]
        if mat[move[0]][move[1]] != "_":
            print("This cell is occupied! Choose another one!")  # if the cell is not empty;
            continue
        mat[move[0]][move[1]] = player
        show_state()
        ack = True


show_state()
g_player = "X"
check_input(g_player)
while not check_winner():
    g_player = "X" if g_player == "O" else "O"
    check_input(g_player)
