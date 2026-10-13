from collections import Counter
import random 

def isWin(userChoice, computerChoice):
    match userChoice:
        case "Rock":
            if computerChoice == "Paper":
                return False
            elif computerChoice == "Scissors":
                return True
            else:
                return None
        case "Scissors":
            if computerChoice == "Rock":
                return False
            elif computerChoice == "Paper":
                return True
            else:
                return None
        case "Paper": 
            if computerChoice == "Scissors":
                return False
            elif computerChoice == "Rock":
                return True
            else:
                return None
        case _:
            print("Invalid Choice")

counters = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}


def easyComputer(userMoverHistory):
    choices = ["Paper", "Scissors", "Rock"]
    return choices[random.randint(0,2)]

def mediumComputer(userMoveHistory):
    choices = ["Paper", "Scissors", "Rock"]
    if not userMoveHistory:
        return choices[random.randint(0,2)]
    weights = {
    "Rock": 0,
    "Paper": 0,
    "Scissors": 0
    }
    for index, move in enumerate(userMoveHistory):
        weights[move] += index + 1
    highestWeight = max(weights.values())
    tiedMoves = [move for move in weights if weights[move] == highestWeight]
    if len(tiedMoves) == 1:
        return counters[tiedMoves[0]]
    else:
        for move in reversed(userMoveHistory):
            if move in tiedMoves:
                return counters[move]

def hardComputer(userMoveHistory):
    choices = ["Paper", "Scissors", "Rock"]
    h, n = userMoveHistory, 3
    for n in range(n, 0, -1):
        if len(h) <= n:
            continue
        pattern = h[-n:]    
        for i in range(len(h) - n - 1, -1, -1):
            if h[i:i + n] == pattern:
                return counters[h[i + n]]
    return choices[random.randint(0,2)]



def playGame():
    userDifficulty = input("Enter Difficulty Level (Easy/Medium/Hard): ")
    userWins = 0
    computerWins = 0
    userMoveHistory = []
    while True:
        difficultiesToComputer = {"Easy": easyComputer, "Medium": mediumComputer, "Hard": hardComputer}            
        userChoice = input("Enter Your Choice (Enter 1 To Quit): ")
        if userChoice == "1":
            break
        userMoveHistory.append(userChoice)
        computerChoice = difficultiesToComputer[userDifficulty](userMoveHistory)
        result = isWin(userChoice, computerChoice)
        print(f"The Computer Chose: {computerChoice}")
        if result is True:
            print("You Won This Round")
            userWins += 1
        elif result is False:
            print("The Computer Won This Round")
            computerWins += 1
        else:
            print("There Was A Tie")
        print(f"Score is {userWins} - {computerWins}")