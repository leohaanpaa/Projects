import random
from words import words
import string

# Function for generating a random word from the list of words that doesn't have spaces or -
def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

# Function for the game logic
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 10
    
    # Play the game until word_letters or lives reaches 0
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives left and have used these letters: ', ' '.join(used_letters))
        
        # Create a list that iterates over the word_letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        # Prints the current state of word using join method
        print('Current word: ', ' '.join(word_list))
        
        # Get user's guess
        user_letter = input('Guess a letter: ').upper()
        
        # Checks if the guessed letter is in alphabet but not in the set of letters already guessed
        if user_letter in alphabet - used_letters:
            
            # Keeps track of what letters has been guessed so far
            used_letters.add(user_letter)
            
            # Checks if the guessed letter is in the word
            if user_letter in word_letters:
                # Removes the guessed letter from the word_letters set
                word_letters.remove(user_letter)
            
            else:
                # If the letter is not in the word, the user loses a life
                lives -= 1
                print("Letter is not in the word")
                
        # If the user has already guessed the letter, print a message
        elif user_letter in used_letters:
            print('You already guessed the letter', user_letter, '- try another one')
            
        else:
            # If the user guesses a letter that is not in the alphabet, print a message
            print("Invalid character")    
            
    # Gets gere when lenght(word_letter) reaches == 0 or when lives == 0
    
    # If the user has run out of lives, print the word and end the game
    if lives == 0:
        print('You died, the word was:', word)
    else:
        # If the user has guessed the word, print the word and end the game
        print('Congratulations, you guessed the word!', word, )

hangman()