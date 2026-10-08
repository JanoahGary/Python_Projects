import random

#Adjusts Game Parameters Based On User Selected Difficulty
def setDifficulty():
    userDifficulty = input("Enter Difficulty Level (Easy/Medium/Hard): ")
    match userDifficulty:
        case "Easy":
            targetRange = (1, 10)
            numOfAttempts = 3
            playGame(numOfAttempts, targetRange)
        case "Medium":
            targetRange = (1, 100)
            numOfAttempts = 3
            playGame(numOfAttempts, targetRange)
        case "Hard":
            targetRange = (1, 1000)
            numOfAttempts = 3
            playGame(numOfAttempts, targetRange)
        case _: 
            print("Invalid Difficulty Selected!")

#Display The Rules To Player
def displayRules():
    userChoice = int(input("Which Game Rules Do You Wish To View?\n1. Guessing Game\n2. Rock Paper Scissors\n3. Hang Man"))
    match userChoice:
        case 1:
            print("The Goal Of The Game Is To Correctly Guess A Random Number In A Certain Range\n" \
            "The Range Of The Target Number Will Depend On Your Selected Difficulty\n" \
            "Your Number Of Attempts Will Stay The Same Regardless Of Difficulty\n")
        case 2:
            print("The Goal Of The Game Is To Correctly Choose The Winning Play Against The Algorithm\n" \
            "The Algorithm Chooses Its Hand Before You Choose Yours, Making The Game Fair\n" \
            "The Algorithm Will Play According To Common Patterns Found In Rock Paper Scissors\n")
        case 3:
            print("The Goal Of The Game Is To Correctly Guess The Word From The Chosen Category\n" \
            "The Length Of The Word Will Depend On Your Selected Difficulty\n" \
            "Your Number Of Attempts Will Scale With Difficulty\n")
        case _:
            print("Invalid Game Choice")

#Display The Game Menu To User
def displayMenu():
    print("Welcome To Games.py!\n1. Play Games\n2. Review Rules\n")
    userChoice = input("Enter Your Choice: ")
    match userChoice:
        case "1":
            setDifficulty()
        case "2":
            displayRules()
        case _:
            print("Invalid Choice")

def playGame(numOfAttempts, targetRange):
    targetNumber = random.randint(*targetRange)
    while numOfAttempts > 0:
        userGuess = int(input("Enter Your Guess: "))
        if userGuess == targetNumber:
            print("You Won! Good Job!")
        elif userGuess != targetNumber and userGuess > targetNumber:
            print("Incorrect Number Guessed\nNumber Is Lower")
            numOfAttempts -= 1
        elif userGuess != targetNumber and userGuess < targetNumber:
            print("Incorrect Number Guessed\nNumber Is Higher")
            numOfAttempts -= 1
    print(f"\nGame Over! {targetNumber} Was The Correct Number")
