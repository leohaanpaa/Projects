import random

def main():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    print(random_number)
    # Ask the user to guess the number
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        # Check if the user's guess is correct
        if int(user_guess) == random_number:
            print("Congratulations, you guessed it correctly!")
            break
        else:
            print("Wrong guess! Do you want to try again?")
            # Ask the user if they want to try again
            try_again = input("Type 'yes' to try again or 'no' to quit: ")
            if try_again.lower() != "yes":
                break
main()