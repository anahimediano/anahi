import random
number= random.randint(1,10)
print("guess a number between 1 and 10.")
     while True:
             number_guess=input("enter your guess (type ´quit´to exit):")
            if inputt.lower()=="quit":
                print("The number was" + number + "Thanks for playing!")
                break 
            try:
            number_guess = int(inputt)
            if number_guess=number
                print("Congratulations! You've guessed the right number!")
                break
            else:
                print("Wrong guess, try again.")

        except ValueError:
            print("Invalid input. Please enter a number or type 'quit' to exit.")
