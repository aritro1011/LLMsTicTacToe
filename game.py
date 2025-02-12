
# Function to initialize the game board
def initialize_board():
    return [' ' for _ in range(9)]  # A list of 9 spaces representing the board

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the game has a winner
def check_winner(board, player):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (i.e., game ends in a tie)
def check_full(board):
    return ' ' not in board

# Function to display the list of filled positions
def show_filled_positions(board):
    filled_positions = [i + 1 for i, cell in enumerate(board) if cell != ' ']
    return filled_positions

# Main function to play the game
def play_game():
    board = initialize_board()
    current_player = 'X'  # Player X starts the game
    while True:
        print_board(board)
        
        # Show filled positions
        filled_positions = show_filled_positions(board)
        print(f"Filled positions: {filled_positions}")
        
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move or position already filled, try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")
            continue
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie game)
        if check_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
