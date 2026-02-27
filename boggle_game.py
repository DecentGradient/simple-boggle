import random
import string
import os

def generate_board(N):
    """
    Creates an NxN 2D list and populates each cell with a random uppercase English letter.
    Returns the generated board.
    """
    return [[random.choice(string.ascii_uppercase) for _ in range(N)] for _ in range(N)]

def load_dictionary(filepath):
    """
    Reads words from the specified filepath, cleans them, converts them to uppercase,
    and stores them in a Python set. Returns the set of valid words.
    """
    valid_words = set()
    if not os.path.exists(filepath):
        print(f"Warning: Dictionary file '{filepath}' not found.")
        return valid_words
        
    with open(filepath, 'r') as f:
        for line in f:
            word = line.strip().upper()
            if word:
                valid_words.add(word)
                
    return valid_words

def display_board(board):
    """
    Prints the NxN board to the console with each letter having a rainbow background.
    """
    # ANSI escape codes for background colors
    colors = [
        "\033[41m", # Red
        "\033[43m", # Yellow
        "\033[42m", # Green
        "\033[46m", # Cyan
        "\033[44m", # Blue
        "\033[45m", # Magenta
    ]
    reset = "\033[0m"

    N = len(board)
    color_idx = 0

    print("\n" + "=" * (N * 4 + 1))
    for row in board:
        line = ""
        for char in row:
            color = colors[color_idx % len(colors)]
            # Add padding around the character for better visual
            line += f"{color} {char} {reset} "
            color_idx += 1
        print(line)
    print("=" * (N * 4 + 1) + "\n")

if __name__ == "__main__":
    N = 4
    board = generate_board(N)
    display_board(board)
