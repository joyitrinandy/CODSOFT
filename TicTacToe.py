import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    if check_win(board, "X"):
        return scores["X"]
    if check_win(board, "O"):
        return scores["O"]
    if is_full(board):
        return scores["tie"]

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move using Minimax with Alpha-Beta Pruning
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = minimax(board, 0, False, alpha, beta)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
                alpha = max(alpha, score)

    return best_move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_full(board):
        row, col = find_best_move(board)
        board[row][col] = "X"
        print("AI's move:")
        print_board(board)
        
        if check_win(board, "X"):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a tie!")
            break
        
        row = int(input("Enter row for your move (0, 1, 2): "))
        col = int(input("Enter column for your move (0, 1, 2): "))
        
        while board[row][col] != " ":
            print("Invalid move. That cell is already occupied.")
            row = int(input("Enter row for your move (0, 1, 2): "))
            col = int(input("Enter column for your move (0, 1, 2): "))
        
        board[row][col] = "O"
        print_board(board)
        
        if check_win(board, "O"):
            print("You win!")
            break

play_game()