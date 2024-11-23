# Handles the core mechanics of the game, including updating the game state based on user input.
# Determine if the guessed letter is in the word.
# Track remaining lives and end the game on win/lose conditions.
# Generate the partially revealed word (e.g., "h _ n g _ a n").
# Maintain a list of incorrect guesses.

import random
from core_modules.input_handling import validate_guess

# Hangman stages as ASCII art
hangman_stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """,
]


def pick_word(word_list):
    """Selects a random word from the provided word list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Generates the current state of the word with guessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_game(word_list):
    """Core logic of the Hangman game."""
    word = pick_word(word_list)
    guessed_letters = set()
    lives = len(hangman_stages) - 1

    while lives > 0:
        # Display the game state
        print(hangman_stages[len(hangman_stages) - 1 - lives])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Lives Left: {lives}")

        # Player input
        guess = input("Enter a letter: ").lower()

        # Input validation and game logic
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
            if set(word) <= guessed_letters:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            lives -= 1
            print("Wrong!")

    # Game over logic
    if lives == 0:
        print(hangman_stages[-1])
        print(f"Game Over! The word was: {word}")
