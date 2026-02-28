def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    for row in board:
        if all([s == player for s in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = current_player
                moves += 1
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tictactoe()