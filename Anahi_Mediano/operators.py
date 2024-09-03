guess=int(input ("Guess a number between 1 and 10:"))
while True:
    if guess == 3:
        print("correct")
        break
    elif guess< 3:
        print("you are guessing too low")
        guess=int(input ("Guess a number between 1 and 10:"))
    elif guess>10:
        print ("between 1 and 10")
        guess=int(input ("Guess a number between 1 and 10:"))
    else:
        print ("you are guessing too high")
        guess=int(input ("Guess a number between 1 and 10:"))
