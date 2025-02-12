import os
from groq import Groq
from config import API_KEY_Groq
import time

# Initialize Groq client
client = Groq(api_key=API_KEY_Groq)

# Function to call Llama 3 model and get a response
def get_groq_move(board, retries=3, temperature=0.5):
    filled_positions = [i + 1 for i, cell in enumerate(board) if cell != ' ']
    context = f"Filled positions: {filled_positions}\nPlayer X, choose a position (1-9):"
    
    task = """You are an expert Tic-Tac-Toe player. Respond with ONLY a single digit 
    (0–9) representing your next move.
    Rules: 
    1. Do NOT repeat moves or choose already filled positions.
    2. Aim to WIN using the current board state and your past moves. 
    3. Deduce your opponent’s moves by comparing filled positions. 
    Respond with just the digit."""

    prompt = f"{task}\n\nContext: {context}"

    try:
        # Create a chat completion request to Groq's Llama 3 model
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=temperature  # Adjusted temperature
        )
        
        # Parse the response from Llama AI
        response = chat_completion.choices[0].message.content.strip()
        ai_move = int(response)  # Convert the response to an integer
        
        # Ensure the move is within the valid range and not a filled position
        if ai_move < 1 or ai_move > 9 or ai_move in filled_positions:
            if retries > 0:
                print(f"Invalid move {ai_move}. Retrying...")
                time.sleep(1)
                return get_groq_move(board, retries - 1, temperature)  # Retry on invalid move
            else:
                print("Max retries exceeded for Llama AI.")
                return 0, temperature  # Return invalid move and temperature
        
        return ai_move, temperature

    except ValueError:
        # Handle case where AI response is not a valid integer
        if retries > 0:
            print("Invalid response from Llama AI. Retrying...")
            time.sleep(1)
            return get_groq_move(board, retries - 1, temperature)  # Retry on invalid response
        print("Error: Invalid move format from Llama AI.")
        return 0, None  # Return invalid move and None on format error

    except Exception as e:
        # Catch all exceptions and retry if possible
        if retries > 0:
            time.sleep(1)
            return get_groq_move(board, retries - 1, temperature)  # Retry on error
        print(f"Error in Llama AI move: {e}")
        return 0, None  # Return invalid move and None
