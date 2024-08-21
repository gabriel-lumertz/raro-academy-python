from random import randrange
from time import sleep
import os

plays = ('Rock', 'Spock', 'Paper', 'Lizard', 'Scissors')

print(
    '''
    Options:
    [ 0 ] ROCK
    [ 1 ] SPOCK
    [ 2 ] PAPER
    [ 3 ] LIZARD
    [ 4 ] SCISSORS
    '''
)

player_one = int(input('Choose a number between 0 and 4? '))

player_two = randrange(0, 4)

os.system('clear')

print('Player chooses {}'.format(plays[player_one]))
print('Computer chooses {}'.format(plays[player_two]))


if player_one == 0: # Jogou pedra
    if player_two == 0:
        print('Player and computer tie!')
    elif player_two == 1 or player_two == 2:
        print('Player wins!')
    elif player_two == 3 or player_two == 4:
        print('Computer wins!')
    else:
        print('Invalid Play')

if player_one == 1: # Jogou spock
    if player_two == 1:
        print('Player and computer tie!')
    elif player_two == 0 or player_two == 4:
        print('Player wins!')
    elif player_two == 2 or player_two == 3:
        print('Computer wins!')
    else:
        print('Invalid Play')

if player_one == 2: # jogou papel
    if player_two == 2:
        print('Player and computer tie!')
    elif player_two == 0 or player_two == 1:
        print('Player wins!')
    elif player_two == 3 or player_two == 4:
        print('Computer wins!')
    else:
        print('Invalid Play')

if player_one == 3: # jogou lagarto
    if player_two == 3:
        print('Player and computer tie!')
    elif player_two == 2 or player_two == 1:
        print('Player wins!')
    elif player_two == 4 or player_two == 0:
        print('Computer wins!')
    else:
        print('Invalid Play')

if player_one == 4: # jogou tesoura
    if player_two == 4:
        print('Player and computer tie!')
    elif player_two == 2 or player_two == 3:
        print('Player wins!')
    elif player_two == 0 or player_two == 1:
        print('Computer wins!')
    else:
        print('Invalid Play')