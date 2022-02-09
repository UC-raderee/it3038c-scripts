import random, math

print('Enter the range of numbers you would like to guess inbetween.  A random number will be generated depending on your input.')

lower = int(input('Enter lowest number:- '))

upper = int(input('Enter highest number:- '))

x = random.randint(lower, upper)

print('\n\tYou have ',
        round(math.log(upper - lower +1, 2)),
        'chances to guess the random number!\n')

count = 0

while count < math.log(upper - lower +1, 2):
    count += 1

    guess = int(input('Guess a number:- '))

    if x == guess:
        print('Congratulations, you guessed the number!')
        break

    elif x > guess:
        print('Oops, your guess was too small.')

    elif x < guess:
        print('Oops, your guess was too large.')

    if count >= math.log(upper - lower +1, 2):
        print("\nThe number is %d" % x)
        print("\tThanks for playing!")

