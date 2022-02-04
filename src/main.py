import random

guessesTaken = 0

print('First, your name ?')
name = input()

toGuess = random.randint(1,20)
print('hi ' + name + ' now its time to guess the number')


for guessesTaken in range(6):
    print('your guess ?')
    guess = input()
    guess = int(guess)

    if (guess < toGuess):
        print('you\'re too low')

    if (guess > toGuess):
        print('you\'re too high')

    if (guess == toGuess):
        break

if (guess == toGuess):
    print('you won !!')
else:
    print('I\m sorry, but you failed. You should have guessed ' + str(toGuess))
