# Random selection of a word.
# Difficulty settings to choose word lengths (e.g., Easy: 4-6 letters, Hard: 10+ letters).
# Option to track used words to avoid repetition.


def load_word_list(file_path="assets/word_list.txt"):
    """Loads the word list from an external text file."""
    with open(file_path, "r") as file:
        words = [line.strip() for line in file.readlines() if line.strip()]
    return words
