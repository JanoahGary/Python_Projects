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

def isWin(userChoice, computerChoice):
    match userChoice:
        case "Rock":
            if computerChoice == "Paper":
                return False
            elif computerChoice == "Scissors":
                return True
            else:
                print("There Was A Tie, Enter Another Choice")
                return None
        case "Scissors":
            if computerChoice == "Rock":
                return False
            elif computerChoice == "Paper":
                return True
            else:
                print("There Was A Tie, Enter Another Choice")
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

def easyComputer():
    choices = ["Paper", "Scissors", "Rock"]
    return choices[random.randint(0, 2)]
def  mediumComputer():
    choices = ["Paper", "Scissors", "Rock"]
    return 0
def hardComputer():
    choices = ["Paper", "Scissors", "Rock"]
    return 0



def playGame():
    userChoice = input("Enter Your Choice")