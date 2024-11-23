# Orchestrates the overall sequence of the game from start to finish.
# Manage the main game loop.
# Check win/loss conditions and terminate the game when appropriate.
# Restart or quit the game upon completion.

from core_modules.game_logic import play_game


def start_game():
    """Handles the overall flow of the game."""
    print("Starting the game...")

    # Temporary word list (will eventually be replaced by an external module)
    word_list = [
        "apple",
        "banana",
        "cherry",
        "orange",
        "kiwi",
        "grape",
        "mango",
        "pineapple",
        "watermelon",
        "lemon",
    ]

    # Start the Hangman game
    play_game(word_list)
