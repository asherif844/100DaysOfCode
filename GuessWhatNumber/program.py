import random 
print('----------------------')
print('   Guess That #       ')
print('----------------------')
print('')

the_number = random.randint(50,100)
name = input('What is your name sir?')
guess = -1


while guess != the_number:
    try:
        guess_text = input('Guess a number between 50 and 100: ')
        guess = int(guess_text)

        if guess < the_number:
            print('Sorry {1}, your guess of {0} is too low!'.format(guess, name))
        elif guess > the_number:
            print('Sorry {1}, your guess of {0} is too high!'.format(guess, name))
        else:
            print('Excellent work {1}, your guess of {0} is accurate!'.format(guess, name))
    except ValueError:
        print('This is not a number, try again')
    
print('done')
