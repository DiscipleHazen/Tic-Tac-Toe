from random import randrange

def display_board(board):
    print(f"+{'-' * 7}+{'-' * 7}+{'-' * 7}+")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")
    print(f"|{' ' * 3}{board[0][0]}{' ' * 3}|{' ' * 3}{board[0][1]}{' ' * 3}|{' ' * 3}{board[0][2]}{' ' * 3}|")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")

    print(f"+{'-' * 7}+{'-' * 7}+{'-' * 7}+")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")
    print(f"|{' ' * 3}{board[1][0]}{' ' * 3}|{' ' * 3}{board[1][1]}{' ' * 3}|{' ' * 3}{board[1][2]}{' ' * 3}|")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")

    print(f"+{'-' * 7}+{'-' * 7}+{'-' * 7}+")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")
    print(f"|{' ' * 3}{board[2][0]}{' ' * 3}|{' ' * 3}{board[2][1]}{' ' * 3}|{' ' * 3}{board[2][2]}{' ' * 3}|")
    print(f"|{' ' * 7}|{' ' * 7}|{' ' * 7}|")
    print(f"+{'-' * 7}+{'-' * 7}+{'-' * 7}+")


def enter_move(board, player, player_input):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    player_input -= 1
    try:
        if 0 <= player_input <= 2:
            if board[0][player_input] == AI_symbol or board[0][player_input] == player_symbol:
                raise ValueError
            else:
                board[0][player_input] = player
                return True

        if 3 <= player_input <= 5:
            if board[1][player_input - 3] == AI_symbol or board[1][player_input - 3] == player_symbol:
                raise ValueError
            else:
                board[1][player_input - 3] = player
                return True

        if 6 <= player_input <= 8:
            if board[2][player_input - 6] == AI_symbol or board[2][player_input - 6] == player_symbol:
                raise ValueError
            else:
                board[2][player_input - 6] = player
                return True

    except ValueError:
            print("Cannot place an O there, place in an empty spot 1-9")



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0].count(sign) == 3 or board[1].count(sign) == 3 or board[2].count(sign) == 3:
        return sign
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return sign
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return sign
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return sign

    return "no win"



board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
display_board(board)

player_symbol = "O"
AI_symbol = "X"

game_over = False
turn_counter = 0

print("Welcome to Tic Tac Toe!")
player_input = input("Enter any key to get started, enter '-1' to quit")
display_board(board)
while not game_over:
    end_turn = False

    while not end_turn:
        player_input = int(input("Enter a move, 1-9: "))
        if player_input == -1:
            print("Quitting...")
            break
        end_turn = enter_move(board, player_symbol, player_input)

    end_turn = False

    while not end_turn:
        print("The AI will now take a turn...")
        end_turn = enter_move(board, AI_symbol, randrange(0, 9))

    display_board(board)

    if victory_for(board, player_symbol) == player_symbol:
        print("YOU WIN!!!")
        game_over = True
    elif victory_for(board, AI_symbol) == AI_symbol:
        print("YOU LOSE!")
        game_over = True
    elif turn_counter == 9:
        print("ITS A DRAW!")
        break
    else:
        continue






