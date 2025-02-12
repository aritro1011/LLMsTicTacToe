import os
from groq import Groq
from config import API_KEY_Groq
import time

# Initialize Groq client
client = Groq(api_key=API_KEY_Groq)

# Function to call Llama 3 model and get a response
def get_groq_move(board, retries=3, temperature=0.2):
    filled_positions = [i + 1 for i, cell in enumerate(board) if cell != ' ']
    context = f"Filled positions: {filled_positions}\nPlayer X, choose a position (1-9):"
    
    task = """You are an expert Tic-Tac-Toe player. Respond with ONLY a single digit 
    (0–9) representing your next move.
    Rules: 
    1. Do NOT repeat moves or choose already filled positions.
    2. Aim to WIN using the current board state and your past moves. 
    3. Deduce your opponent’s moves by comparing filled positions. 
    Focus on smart, winning moves. 
    Respond with just the digit."""

    prompt = f"{task}\n\nContext: {context}"

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=temperature  # Adjusted temperature
        )
        response = chat_completion.choices[0].message.content.strip()
        ai_move = int(response)
        if ai_move < 1 or ai_move > 9:
            if retries > 0:
                time.sleep(1)
                return get_groq_move(board, retries - 1, temperature)  # Retry if invalid response
            else:
                print("Max retries exceeded for Llama AI.")
                return 0, temperature  # Return invalid move and temperature
        return ai_move, temperature
    except Exception as e:
        if retries > 0:
            time.sleep(1)
            return get_groq_move(board, retries - 1, temperature)  # Retry on error
        print(f"Error in Llama AI move: {e}")
        return 0, None  # Return invalid move and None
