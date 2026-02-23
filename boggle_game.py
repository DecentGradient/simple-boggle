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
