import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        return 'treasure'
    else:
        return 'gobble'

def oh(friendlyCave, chosenCave):
    otherCave = '1' if friendlyCave == 2 else '2'
    print(f"You would have chosen cave {otherCave}, and here is what would have happened...")
    
    # Simulate the outcome of the other cave
    time.sleep(2)
    if otherCave == str(friendlyCave):
        print('The dragon in the other cave would have given you his treasure!')
    else:
        print('The dragon in the other cave would have gobbled you down in one bite!')

playAgain = 'yes'
while playAgain.lower() in ['yes', 'y']:
    displayIntro()
    caveNumber = chooseCave()
    result = checkCave(caveNumber)
    
    if result == 'treasure':
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
        print('Do you want to know what would have happened if you had chosen the other cave? (yes or no)')
        if () in ['yes', 'y']:
            friendlyCave = 1 if caveNumber == '2' else 2
            oh(friendlyCave, caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input().lower()
    
    