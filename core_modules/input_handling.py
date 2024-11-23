# Captures and validates user iCaptures and validates user input during the game.
# Ensures the entered input is a valid guess (single letter or full word, no numbers/symbols).
# Check if input is valid (e.g., only letters).
# Handle case insensitivity.
# Record already guessed letters to prevent duplication.


def validate_guess(guessed_letters):
    """Validates and processes user input for guesses."""
    while True:
        guess = input("Enter a letter: ").lower()

        # Ensure input is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another.")
        else:
            return guess
