import getpass 

numberToGuess1 = int(getpass.getpass("Number to guess: "))
rightNumber = int(input("Guess the number: "))  

while rightNumber != numberToGuess1:
    rightNumber= int(input("Guess the number: ")) 
    if rightNumber == numberToGuess1:
        print("You guest the number congratulation", rightNumber)