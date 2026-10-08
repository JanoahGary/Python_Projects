import random

def setDifficulty():
    userDifficulty = input("Enter Difficulty Level (Easy/Medium/Hard): ")
    match userDifficulty:
        case "Easy":
            0
        case "Medium":
            0
        case "Hard":
            0
        case _: 
            print("Invalid Difficulty Selected!")

def isWin():
    userChoice = input("Enter Your Choice (Rock/Paper/Scissors)")
    match userChoice:
        case "Rock":
            0