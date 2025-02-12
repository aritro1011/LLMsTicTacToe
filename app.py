import random
import csv
import os
from game import initialize_board, print_board, check_winner, check_full, show_filled_positions
from Player_Gemini import get_ai_move as gemini_ai_move  # Import the Gemini-based AI player
from Player_Llama import get_groq_move  # Import the Groq-based AI player from Player_Llama

# Function to perform a toss to decide which AI starts the game
def toss():
    if random.choice([True, False]):
        print("Llama AI wins the toss and will start as Player X.")
        return ('X', get_groq_move, gemini_ai_move, 'Llama AI', 'Gemini AI')
    else:
        print("Gemini AI wins the toss and will start as Player X.")
        return ('X', gemini_ai_move, get_groq_move, 'Gemini AI', 'Llama AI')

# Function to log game results to a CSV file
def log_result(result):
    try:
        file_exists = os.path.isfile('game_results.csv')
        with open('game_results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Llama_Win', 'Gemini_Win', 'Tie', 'Total_Moves', 'First_Player', 'First_Move_Position', 'Move_Sequence', 'GeminiTemperature', 'LlamaTemperature'])
            writer.writerow(result)
    except IOError as e:
        print(f"Error writing to file: {e}")

# Function to analyze the first move position (corner, center, edge)
def analyze_opening_move(move):
    if move in [1, 3, 7, 9]:  # corners
        return "Corner"
    elif move == 5:  # center
        return "Center"
    else:  # edges
        return "Edge"

# Function to play a single game
def play_game(log_results):
    board = initialize_board()
    current_player, player_x_func, player_o_func, player_x_name, player_o_name = toss()  # Perform the toss
    first_move = None
    first_player = player_x_name  # Store the first player at the start
    move_sequence = []  # To track the sequence of moves
    gemini_temp = 0.0  # Store Gemini temperature
    llama_temp = 0.0  # Store Llama temperature

    while True:
        print_board(board)

        # Show filled positions
        filled_positions = show_filled_positions(board)
        print(f"Filled positions: {filled_positions}")

        if current_player == 'X':
            ai_move, gemini_temp = player_x_func(board)  # Get Player X's move
            if ai_move is None:
                print("Invalid move by Gemini AI. Retrying.")
                continue
            ai_move = int(ai_move)
            print(f"Player {current_player} ({player_x_name}) chose position {ai_move}")
            board[ai_move - 1] = current_player
        else:
            ai_move, llama_temp = player_o_func(board)  # Get Player O's move
            if ai_move is None:
                print("Invalid move by Llama AI. Retrying.")
                continue
            ai_move = int(ai_move)
            print(f"Player {current_player} ({player_o_name}) chose position {ai_move}")
            board[ai_move - 1] = current_player

        # Record the first move
        if first_move is None:
            first_move = ai_move
            opening_move_position = analyze_opening_move(first_move)

        move_sequence.append(ai_move)

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            winner = player_x_name if current_player == 'X' else player_o_name
            print(f"Player {current_player} ({winner}) wins!")

            # Log result if enabled
            total_moves = len(move_sequence)
            if log_results:
                result = [0, 0, 0, total_moves, first_player, opening_move_position, '-'.join(map(str, move_sequence)), gemini_temp, llama_temp]
                if winner == 'Llama AI':
                    result[0] = 1  # Llama win
                else:
                    result[1] = 1  # Gemini win
                log_result(result)
            break

        # Check if the board is full (tie game)
        if check_full(board):
            print_board(board)
            print("It's a tie!")

            # Log tie if enabled
            total_moves = len(move_sequence)
            if log_results:
                result = [0, 0, 1, total_moves, first_player, opening_move_position, '-'.join(map(str, move_sequence)), gemini_temp, llama_temp]  # Tie
                log_result(result)
            break

        # Switch player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    log_choice = input("Do you want to log the game results? (yes/no): ").strip().lower()
    while log_choice not in ['yes', 'no']:
        log_choice = input("Invalid input. Please enter 'yes' or 'no': ").strip().lower()
    log_results = log_choice == 'yes'

    # Ask for the number of matches after logging choice
    num_matches = input("How many matches would you like the agents to play one after another? (Enter a number): ").strip()
    while not num_matches.isdigit() or int(num_matches) <= 0:
        num_matches = input("Invalid input. Please enter a positive number: ").strip()
    
    num_matches = int(num_matches)

    # Loop through the specified number of matches
    for match in range(num_matches):
        print(f"\n--- Match {match + 1} ---")
        play_game(log_results)
    print(f"Completed {num_matches} matches.")
