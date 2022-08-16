#! python3
#Shebang Line ( es la linea de arriba, con esto puedo ejecutarlo como escript)

# This is a guess the number game.

import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')

# ASk the player to guess 6 times.
for guessesTaken in range(1,7):
    
    if guessesTaken<2:
        print('Take a guess.')
    else:
        print('Try again!S')

    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in '+ str(guessesTaken) + ' shots!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))