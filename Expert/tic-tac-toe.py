def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input():
    while True:
        try:
            # Prompt the user for input
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        # Get valid input
        row, col = get_valid_input()

        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Cell is already occupied, try again!")

tic_tac_toe()
