import google.generativeai as genai
from config import API_KEY_Gemini
import time

# Configure Gemini API
genai.configure(api_key=API_KEY_Gemini)

# Function to call Gemini to make a move based on current board state
def get_ai_move(board, retries=3):
    filled_positions = [i + 1 for i, cell in enumerate(board) if cell != ' ']
    context = f"Filled positions: {filled_positions}\nPlayer X, choose a position (1-9):"

    task = """You are an expert Tic-Tac-Toe player.
                Respond with ONLY a single digit (0–9) representing your next move.
                Rules: 
                1. Do NOT repeat moves or choose already filled positions. 
                2. Aim to WIN using the current board state and your past moves. 
                3. Deduce your opponent’s moves by comparing filled positions.
                Focus on smart, winning moves.  
                Focus on smart, winning moves. 
                Respond with just the digit."""

    # Send the prompt and context to Gemini to generate the AI's move
    try:
        response, temperature = call_gemini(task, context)
        ai_move = int(response.strip())

        # Ensure the move is within the valid range and not already filled
        if ai_move < 1 or ai_move > 9 or ai_move in filled_positions:
            if retries > 0:
                print(f"Invalid move {ai_move}. Retrying...")
                time.sleep(1)  # Sleep to prevent overwhelming the API
                return get_ai_move(board, retries - 1)  # Retry if invalid move
            else:
                print("Max retries exceeded for Gemini AI.")
                return 0, temperature  # Return invalid move and temperature

        return ai_move, temperature

    except ValueError:
        # Handle case where AI response is not a valid integer
        if retries > 0:
            print("Invalid response from Gemini AI. Retrying...")
            time.sleep(1)
            return get_ai_move(board, retries - 1)  # Retry on invalid response
        print("Error: Invalid move format from Gemini AI.")
        return 0, None  # Return invalid move and None

    except Exception as e:
        # Catch all exceptions and retry if possible
        if retries > 0:
            time.sleep(1)
            return get_ai_move(board, retries - 1)  # Retry on error
        print(f"Error in Gemini AI move: {e}")
        return 0, None  # Return invalid move and None

def call_gemini(task, context, temperature=0.5):
    prompt = f"{task}\n\nContext:\n{context}"
    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(
            prompt,
            generation_config={"temperature": temperature}
        )
        return response.text.strip(), temperature  # Return both generated text and temperature
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "", None  # Return empty response and None on failure
