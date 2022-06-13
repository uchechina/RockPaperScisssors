import random
gameOptions = ["R", "P", "S"]
transOptions = ["Rock", "Paper", "Scissors"]

print("Welcome to my simple CLI Rock, Paper, Scissors game.")
print("These are the rules: \nRock beats Scissors\nPaper beats Rock\nScissors beats Paper")
print("Select R for Rock, P for Paper, and S for scissors")
userInput = ""

isWinner = False
while (isWinner == False):
    userInput = input("Pick an option between R, P or S\n").upper()
    computerInput = random.choice(gameOptions)
    while userInput not in gameOptions:
        print("Error! Select a valid option")
        userInput = input("Pick an option between R, P or S\n").upper()

    userInput = transOptions[gameOptions.index(userInput)]
    computerInput = transOptions[gameOptions.index(computerInput)]

    print("Player({}) : CPU({})".format(userInput, computerInput))


    if userInput == computerInput:
        print("That's a Tie!")
    elif userInput == "Rock":
        if computerInput == "Paper":
            print("Computer Wins! Better Luck Next Time")
            isWinner = True
        if computerInput == "Scissors":
            print("Congratulations! Player wins")
            isWinner = True
    elif userInput == "Paper":
        if computerInput == "Scissors":
            print("Computer Wins! Better Luck Next Time")
            isWinner = True
        if computerInput == "Rock":
            print("Congratulations! Player wins")
            isWinner = True
    else:
        if computerInput == "Rock":
            print("Computer Wins! Better Luck Next Time")
            isWinner = True
        if computerInput == "Paper":
            print("Congratulations! Player wins")
            isWinner = True

