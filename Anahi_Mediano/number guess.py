import random
number= random.randint(1,10)
print ("guess a number between 1 and 10:")
while True:
    number_guess=input("enter your guess(type quit to exit):")
    print ("The number was" + [number])
    break
if number_guess == number
    print ("Congratualations! you´ve guessed the right number!")
    break
else:
    print("wrong guess, try again.")
except ValueError:
    print("Invalid input. Please enter a number or type quit to exit")