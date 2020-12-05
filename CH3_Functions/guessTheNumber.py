#This is a guess the number game

import random
secretNumber = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

#ask the player to guess 6 times

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Thats too damn low')
    elif guess > secretNumber:
        print('Thats too damn high')
    else:
        break #that means it's the right number

if guess == secretNumber:
    print('YOU GOT IT and it took you ' + str(guessesTaken) + ' tries.')
else:
    print('You are a moron. The number was ' + str(secretNumber))
