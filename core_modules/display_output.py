# Show the current state of the word (e.g., "_ _ t t e r").
# Display lives/tries remaining.
# Provide feedback for each guess (correct/incorrect).
# Show win/loss messages at the end of the game.


def display_message(message):
    """Displays a simple message."""
    print(message)


def display_game_state(hangman_stages, lives, word, guessed_letters):
    """Displays the current game state, including hangman, word, guessed letters, and lives."""
    print(hangman_stages[len(hangman_stages) - 1 - lives])
    print(
        f"\nWord: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}"
    )
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
    print(f"Lives Left: {lives}")
