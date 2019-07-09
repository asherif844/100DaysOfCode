import random

# these are the movies that the computer will be performing
moves = ['rock', 'paper', 'scissors']

# create a switch for the game

keep_playing = 'true'

while keep_playing == 'true':

    # have the computer make a random selection of moves
    cmove = random.choice(moves)

    # have the player pick their move as well
    pmove = input('What is your move: [R]ock, [P]aper, or [S]cissors?')
    print('The computer chose {}'.format(pmove))
    if cmove == pmove:
        print("It's a Tie!")
