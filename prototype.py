import random

# Prototype Word List
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


# Function to pick a random word
def pick_word():
    return random.choice(word_list)


# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


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


# Main Game Logic
def play_game():
    word = pick_word()
    guessed_letters = set()
    lives = len(hangman_stages) - 1

    print("Welcome to Hangman!")
    while lives > 0:
        print(hangman_stages[len(hangman_stages) - 1 - lives])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Lives Left: {lives}")
        guess = input("Enter a letter: ").lower()

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

    if lives == 0:
        print(hangman_stages[-1])
        print(f"Game Over! The word was: {word}")


play_game()
