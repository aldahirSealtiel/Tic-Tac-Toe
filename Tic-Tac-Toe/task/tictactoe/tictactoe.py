# write your code here
def check_win(board, character):
    for i in range(3):
        count_row = 0
        count_column = 0
        for j in range(3):
            if board[i][j] == character:
                count_row += 1
            if board[j][i] == character:
                count_column += 1
        if count_row == 3:
            return True
        if count_column == 3:
            return True
    if board[0][0] == board[1][1] == board[2][2] == character:
        return True
    if board[0][2] == board[1][1] == board[2][0] == character:
        return True
    return False


def count_empty_cells(board):
    ans = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                ans += 1
    return ans


def count_character_cells(board, character):
    ans = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == character:
                ans += 1
    return ans


def print_board(game_board):
    print("---------")
    count_character = 0
    for i in range(3):
        print("| " + " ".join(x for x in game_board[i]) + " |")
        count_character += 3
    print("---------")


board_game = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

print_board(board_game)
piece = 0
while 1:
    row_board = 0
    column_board = 0
    isCorrect = False
    while not isCorrect:
        data_input = input("Enter the coordinates:").split()

        if len(data_input) == 2 and data_input[0].isnumeric() and data_input[1].isnumeric():
            row_board = int(data_input[1])
            column_board = int(data_input[0])
        else:
            print("You should enter numbers!")
            continue

        if not(1 <= row_board <= 3) or not(1 <= column_board <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        row_board = 3 - row_board
        column_board = column_board-1

        if board_game[row_board][column_board] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        isCorrect = True
        if piece == 0:
            board_game[row_board][column_board] = 'X'
        else:
            board_game[row_board][column_board] = 'O'
        piece = (piece + 1) % 2
        print_board(board_game)
    number_empty_cells = count_empty_cells(board_game)

    winX = False
    winY = False

    winX = check_win(board_game, "X")

    winY = check_win(board_game, "O")

    if winX and not winY:
        print("X wins")
        break
    if not winX and winY:
        print("O wins")
        break
    if not winX and not winY and number_empty_cells == 0:
        print("Draw")
        break






