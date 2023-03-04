from random import randint 

rightNumber = randint(0,11)
numberToGuess = int(input("Guess the number (0-10): ")) 

while rightNumber != numberToGuess:
    numberToGuess = int(input("Guess the number: ")) 
    if rightNumber == numberToGuess:
        print("You guest the number congratulation", rightNumber)