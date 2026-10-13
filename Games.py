import GuessingGameFunctions
import RockPaperScissorsFunctions

#Display The Game Menu To User
def displayMenu():
    while True:
        print("Welcome To Games.py!\n1. Play Games\n2. Review Rules\n3. Exit\n")
        userChoice = input("Enter Your Choice: ")
        match userChoice:
            case "1":
                userGameChoice = input("Which Game Do You Want To Play? ")
                match userGameChoice:
                    case "Guessing Game":
                       GuessingGameFunctions.setDifficulty()
                    case "Rock Paper Scissors":
                        RockPaperScissorsFunctions.playGame()
            case "2":
                GuessingGameFunctions.displayRules()
            case "3":
                break
            case _:
                print("Invalid Choice")

displayMenu()