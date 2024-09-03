import random

number_1 = random.randint(1, 10)
print('to exit the program use "exit"')
while True:
    number = input('Guess a number between 1 and 10: ')
    
    if number == 'exit':
        print('you quit the game thankyou!!')
        break
    number = int(number)

    if number < 1 or number > 10:
        print('you have to pick a number between 1 and 10')
    elif number == number_1:
        print('¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡YOU GUESSED RIGHT!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        break
    elif number < number_1:
        print('is to low, try again')
    else:
        print('is to high, try again')
