# Import random from python library
import random

# Function to generate a random number between 1 and 100
def guess(x):
    
    # Generate a random number between 1 and 100
    random_number = random.randint(1, x)
    
    # Set guess count to 0 so the user can't guess 0
    guess = 0
    
    # While loop to check if the guess corresponds the random number
    while guess != random_number:
        
        # Input user 's guess
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        # If guess is lower than random number prompt to try again
        if guess < random_number:
            print("Too low! Guess again.")
            
        # If guess is higher than random number prompt to try again
        elif guess > random_number:
            print("Too high! Guess again.")
    # When user guessess the correct number print        
    print(f"Congrats. You guessed the random number {random_number}")

# Create function to computer guesses users number
def computer_guess(x):
    # Set lowest number
    low = 1
    
    # Set highest number x
    high = x
    
    # Create an empty variable feedback
    feedback = ""
    
    # While loop until feedback is c = correct
    while feedback != "c":
        
        # If low is equal to high then guess the middle number
        if low != high:
            guess = random.randint(low, high)
            
        # Else guess is low or high
        else:
            guess == low # Or high
        
        # Input users opinion is {guess} too high, low or correct
        feedback =  input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        # If feedback is higher then set high to guess + 1
        if feedback == "h":
           high = guess - 1
        
        # If feedback is lower then set low to guess - 1
        elif feedback == "l":
            low = guess + 1
    # When user inputs C and the {guess} is correct print
    print(f"Computer guessed your number, {guess}, correctly!")
        
    
# Call the function
computer_guess(10)