import random

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


# The rest of your code for categories and game functionality.
def load_words(file_path): # Loads words from a text file
    word_bank = {}
    current_category = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):  # Category line
                current_category = line[1:].strip()  # Remove "# " and whitespace
                word_bank[current_category] = {}
            elif ":" in line:  # Difficulty and words line
                difficulty, words = line.split(":")
                difficulty = difficulty.strip()
                words = [word.strip() for word in words.split(",")]
                word_bank[current_category][difficulty] = words
    return word_bank

def get_word(word_bank, category, difficulty, used_words): 
    """Get a random word from the specified category and difficulty.""" 
    if category not in word_bank: 
        raise ValueError(f"Category '{category}' not found.") 
    if difficulty not in word_bank[category]: 
        raise ValueError(f"Difficulty '{difficulty}' not found in category '{category}'.") 
    
    potential_words = [word for word in word_bank[category][difficulty] if word not in used_words] 
    if not potential_words: 
        print(f"No more words available in category '{category}' with difficulty '{difficulty}'.") 
        return None 
    word = random.choice(potential_words) 
    used_words.add(word) 
    return word



def display_word(word, guessed_letters): 
    """Returns the current state of the word with guessed letters revealed.""" 
    return " ".join([letter if letter in guessed_letters else "_" for letter in word]) 

def display_board(missed_letters, correct_letters, secret_word): 
    """Display the current state of the hangman.""" 
    print(hangman_stages[len(missed_letters)]) 
    print() 
    print('Missed letters:', ' '.join(missed_letters)) 
    print('Word:', display_word(secret_word, correct_letters)) 
    print()


def get_guess(already_guessed): 
    """Prompts the player to guess a letter.""" 
    while True: 
        guess = input("Guess a letter: ").lower() 
        if len(guess) != 1: 
            print("Please enter a single letter.") 
        elif guess in already_guessed: 
            print("You have already guessed that letter. Choose again.") 
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': 
            print("Please enter a LETTER.") 
        else: 
            return guess 
        
def play_again(): 
    """Asks if the player wants to play again.""" 
    return input("Do you want to play again? (yes or no): ").lower().startswith('y') 

def main(): 
    print("H A N G M A N")
    word_bank = load_words(r"word_bank.txt")  # Load the word bank

    # Load words for each category 
   # categories = { 
        #'animals': load_words('animals.txt'), 
       # 'sports': load_words('sports.txt'), 
      #  'fruits': load_words('fruits.txt'), 
      #  'colors': load_words('colors.txt'), 
      #  'countries': load_words('countries.txt') 
   # } 
    
    # Print loaded word banks for debugging 
   # for category, word_bank in categories.items(): 
      #  print(f"{category} word bank: {word_bank}")

    #categories = [cat.lower() for cat in word_bank.keys()] - Marie provided the code but need to removed
    #difficulty = ["easy","medium","hard"] - Marie provided the code but need to removed
                  
    categories = list(word_bank.keys()) # Extract categories from word bank 
    difficulties = ["easy", "medium", "hard"]

    used_words = set()

    while True: 
        # Select a category 
        print("Choose a Category: " + ", ".join(categories))
        #print("Choose a Category: Animals, Sports, Fruits, Colors, Countries") 
        category = input().lower() 
        if category in categories: 
           # word_bank = categories[category] 
            break 
        else: 
            print("Invalid choice. Please choose from the available categories.") 
            continue
        
    while True: 
        # Select difficulty level 
        print("Choose a difficulty: Easy, Medium, Hard") 
        difficulty = input().lower() 
        if difficulty in difficulties: 
            secret_word = get_word(word_bank, category, difficulty, used_words) 
            if secret_word: 
                break 
            else: 
                print(f"No more words available in category '{category}' with difficulty '{difficulty}'. Please select another difficulty.") 
                continue                
        else: 
            print("Invalid difficulty. Please choose Easy, Medium, or Hard.") 
            continue


    missed_letters = '' 
    correct_letters = '' 
    game_is_done = False

    while True: 
        display_board(missed_letters, correct_letters, secret_word) 
        guess = get_guess(missed_letters + correct_letters) 
        
        if guess in secret_word: 
            correct_letters += guess 
            
            if all(letter in correct_letters for letter in secret_word): 
                print(f"Yes! The secret word is '{secret_word}'! You have won!") 
                game_is_done = True 
                
        else: 
            missed_letters += guess 
            
            if len(missed_letters) == len(hangman_stages) - 1: 
                display_board(missed_letters, correct_letters, secret_word) 
                print(f"You have run out of guesses! The word was '{secret_word}'.") 
                game_is_done = True 
                
                
        if game_is_done: 
            if play_again(): 
                # Reset game state for a new game 
                #used_words.add(secret_word) # Avoid repetition 
                missed_letters = '' 
                correct_letters = '' 
                game_is_done = False 
                while True: 
                    print("Choose a Category: " + ", ".join(categories) )
                    category = input().lower() 
                    if category in categories: 
                        break
                    else:
                        print("Invalid choice. Please choose from the available categories.")
                        continue

                while True:
                    print("Choose a difficulty: Easy, Medium, Hard")
                    difficulty = input().lower()
                    if difficulty in difficulties:
                        secret_word = get_word(word_bank, category, difficulty, used_words)
                        if secret_word:
                            break
                        else: 
                            print(f"No more words available in category '{category}' with difficulty '{difficulty}'. Please select another difficulty.") 
                            continue
                    else:
                        print("Invalid difficulty. Please choose Easy, Medium, or Hard.")
                        continue
            else:
                break

if __name__ == "__main__":
    main()







