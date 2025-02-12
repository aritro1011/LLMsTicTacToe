# LLM-Based Tic-Tac-Toe

This project implements a Tic-Tac-Toe game played between two AI agents, powered by two large language models (LLMs): Google Gemini and Llama 3 from Groq. The AI agents play against each other with the goal of winning based on their strategic decisions. The game also includes functionality to log game results to a CSV file.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Usage](#usage)
- [Game Features](#game-features)
- [AI Players](#ai-players)
- [Logging Results](#logging-results)
- [Requirements](#requirements)


## Overview

This project is an interactive Tic-Tac-Toe game in which two AI players take turns to make moves and compete to win the game. The game logic allows for the use of two powerful AI models:

- Gemini AI (Powered by Google)
- Llama 3 AI (Powered by Groq)

The game records detailed game results such as moves, temperatures, and game outcomes, storing this data in a CSV file for analysis.



## Sample Output

Here's an example of how a game plays out:

> **Game Initialization:**
```
Do you want to log the game results? (yes/no): yes
Llama AI wins the toss and will start as Player X.
```

### Initial Board:
```
  |   |  
---------
  |   |  
---------
  |   |  
```
**Filled positions:** `[]`

### Move 1 - Player X (Llama AI)
*Chose position 5*
```
  |   |  
---------
  | X |  
---------
  |   |  
```
**Filled positions:** `[5]`

### Move 2 - Player O (Gemini AI)
*Chose position 9*
```
  |   |  
---------
  | X |  
---------
  |   | O
```
**Filled positions:** `[5, 9]`

### Move 3 - Player X (Llama AI)
*Chose position 7*
```
  |   |  
---------
  | X |  
---------
X |   | O
```
**Filled positions:** `[5, 7, 9]`

### Move 4 - Player O (Gemini AI)
*Chose position 1*
```
O |   |  
---------
  | X |  
---------
X |   | O
```
**Filled positions:** `[1, 5, 7, 9]`

### Move 5 - Player X (Llama AI)
*Chose position 8*
```
O |   |  
---------
  | X |  
---------
X | X | O
```
**Filled positions:** `[1, 5, 7, 8, 9]`

### Move 6 - Player O (Gemini AI)
*Chose position 3*
```
O |   | O
---------
  | X |  
---------
X | X | O
```
**Filled positions:** `[1, 3, 5, 7, 8, 9]`

### Move 7 - Player X (Llama AI)
*Chose position 4*
```
O |   | O
---------
X | X |  
---------
X | X | O
```
**Filled positions:** `[1, 3, 4, 5, 7, 8, 9]`

### Move 8 - Player O (Gemini AI)
*Chose position 2*
```
O | O | O
---------
X | X |  
---------
X | X | O
```

### Game Result
**🏆 Player O (Gemini AI) wins!**



## Installation

To run this project, you'll need to have Python installed on your system along with the necessary dependencies.

Step-by-step installation guide:

1. Clone the repository:
```bash
git clone https://github.com/your-username/aritro1011-llmstictactoe.git
cd aritro1011-llmstictactoe
```

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API keys:
   - Obtain API keys for Google Gemini and Groq.
   - Add your API keys to the Config.py file:
```python
API_KEY_Groq = "ADD_GROQ_API_KEY_HERE"
API_KEY_Gemini = "ADD_GEMINI_API_KEY_HERE"
```

## Project Structure

The project directory structure is as follows:

```
└── aritro1011-llmstictactoe/
    ├── Config.py             # Contains API keys for Google Gemini and Groq
    ├── Player_Gemini.py      # Functions for interacting with Google Gemini API
    ├── Player_Llama.py       # Functions for interacting with Groq's Llama API
    ├── app.py                # Main script to play the game
    ├── game.py               # Contains the game logic (e.g., initializing the board)
    ├── game_results.csv      # CSV file that stores game results
    └── requirements.txt      # Python dependencies
```

Description of Files:
- `Config.py`: Holds the API keys for the Gemini and Groq APIs.
- `Player_Gemini.py`: Contains the logic to interact with the Google Gemini AI model and make moves.
- `Player_Llama.py`: Contains the logic to interact with the Groq Llama 3 AI model and make moves.
- `app.py`: Main entry point for the game. It orchestrates the game flow and decides which AI starts the game based on a toss.
- `game.py`: Contains utility functions like board initialization, printing the board, checking for winners, and displaying filled positions.
- `game_results.csv`: Stores the game results such as the winner, the first move, the move sequence, and the temperatures of the AIs.
- `requirements.txt`: Lists the necessary Python dependencies for the project.

## Usage

1. Start the game:
   - Run the app.py file to start the game:
```bash
python app.py
```

2. Log Game Results:
   - When prompted, you can choose whether or not to log the game results to a CSV file.
   - The game results will be logged to game_results.csv, including:
     - Winner (Llama AI or Gemini AI)
     - The first move position (Corner, Edge, Center)
     - The sequence of moves made by both players
     - The temperature used for both AIs' decisions

3. Game Flow:
   - The game will alternate between the two AI players, making their moves until either one wins or the board is full, resulting in a tie.
   - The AI players are configured to aim for smart, winning moves based on the current game board state.

## Game Features

- **AI vs AI Gameplay**: The game is played between two AI models. It does not require user input during gameplay.
- **Smart AI Decisions**: The AI players make decisions based on their past moves and the current state of the game.
- **Move Logging**: Game moves, AI temperatures, and results are logged to a CSV file for analysis.
- **Temperature Control**: The AIs use configurable temperature values to control the randomness of their decisions.

## AI Players

### Gemini AI:
- Powered by Google's Gemini model, it generates responses based on the game context and makes strategic decisions.
- The AI player aims to win and avoid repeating moves.

### Llama AI:
- Powered by Groq's Llama 3 model, it also generates strategic responses and decisions to play Tic-Tac-Toe.
- Similar to Gemini, it aims to win and prevent making invalid or repeated moves.

## Logging Results

Game results are logged in the game_results.csv file.
The file includes:
- **Llama_Win**: Number of wins by Llama AI.
- **Gemini_Win**: Number of wins by Gemini AI.
- **Tie**: Number of tie games.
- **Total_Moves**: Total moves made in the game.
- **First_Player**: The AI that started the game.
- **First_Move_Position**: The position of the first move (Corner, Center, Edge).
- **Move_Sequence**: A sequence of the moves made during the game.
- **GeminiTemperature**: The temperature used for the Gemini AI.
- **LlamaTemperature**: The temperature used for the Llama AI.

## Requirements

You will need the following dependencies to run this project:
- `groq`: The Groq library to interact with the Llama 3 API.
- `google-generativeai`: The Google library to interact with the Gemini API.
- `time`: For managing retries and delays between AI requests.
- `csv`: For logging the game results in a CSV format.

To install the dependencies, simply run:
```bash
pip install -r requirements.txt
```
