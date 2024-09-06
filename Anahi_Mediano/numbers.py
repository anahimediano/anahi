import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")
    while True:
        try:
            user_input = input("Enter your guess (or type 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print(f"The number was {number_to_guess}. Thanks for playing!")
                break
            
            guess = int(user_input)
            
            if guess == number_to_guess:
                print("Congratulations! You've guessed the right number!")
                break
            else:
                print("Wrong guess, try again.")

        except ValueError:
            print("Invalid input. Please enter a number or type 'quit' to exit.")



