import random

def play():
    choices = ['r', 'p', 's']
    computer = random.choice(choices)
    player = input('Zadej r/m/n: ')
    if computer == 'r' and player == 'p':
        return 'you won'
    if computer == 's' and player == 'r':
        return 'you won'
    if computer == 'p' and player == 's':
        return 'you won'
    if computer ==  player:
        return 'draw'
    return 'you lost'

print(play())
