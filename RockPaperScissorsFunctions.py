from collections import Counter
import random 

def playGames():
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

def isWin(userChoice, computerChoice):
    match userChoice:
        case "Rock":
            if computerChoice == "Paper":
                return False
            elif computerChoice == "Scissors":
                return True
            else:
                print("There Was A Tie")
                return None
        case "Scissors":
            if computerChoice == "Rock":
                return False
            elif computerChoice == "Paper":
                return True
            else:
                print("There Was A Tie")
                return None
        case "Paper": 
            if computerChoice == "Scissors":
                return False
            elif computerChoice == "Rock":
                return True
            else:
                print("There Was A Tie, Enter Another Choice")
                return None
        case _:
            print("Invalid Choice")

counters = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}


def easyComputer():
    choices = ["Paper", "Scissors", "Rock"]
    return random.choices(choices)

def mediumComputer(userMoveHistory):
    return counters[Counter(userMoveHistory).most_common(1)[0][0]]

def hardComputer(userMoveHistory):
    choices = ["Paper", "Scissors", "Rock"]
    h, n = userMoveHistory, 3
    if len(h) > n:
        pattern = h[-n:]
        for i in range(len(h) - n - 1, -1, -1):
            if h[i:i + n] == pattern:
                return h[i + n]
    return random.choice(choices)



def playGame(userDifficulty):
    userWins = 0
    computerWins = 0
    if userDifficulty == "Easy":
        while True:
            userMoveHistory = []
            userChoice = input("Enter Your Choice (Enter 1 To Quit):")
            if userChoice == "1":
                break
            userMoveHistory.append(userChoice)
            computerChoice = easyComputer()
            if isWin(userChoice, computerChoice) == True:
                print("You Won This Round")
                userWins += 1
            else:
                print("The Computer Won This Round")
                computerWins += 1
            print(f"Score is {userWins} - {computerWins}")