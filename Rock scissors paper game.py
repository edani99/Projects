import random

# Create a variable and name it something like "computerChoice". Store a random integer between 1 and 3 in the variable.
computerChoice = int(random.randint(1, 3))

# Ask the user for their choice (if they choose rock, make them type 1, if they choose paper, make them type 2, and if they choose scissors, make them type 3)
userChoice = int(input("Enter 1 for rock, 2 for paper, and 3 for scissors: "))

# Check if the user entered a number between 1 and 3. If they didn't, then tell them that they have to restart and to "follow instructions"
if userChoice < 1 or userChoice > 3:
    print("You have to restart and follow instructions")
else:
    # If the user entered a number between 1 and 3, then check if the user and computer chose the same thing. If they did, then tell them that it's a tie.
    if userChoice <= 3 and computerChoice == userChoice:
        print("It is a tie")
    else:
        # Print out the computer's choice (rock if the random integer was 1, paper if the random integer was 2, and scissors if the random integer was 3)
        if computerChoice == 1:
            print("Computer chose rock")
        elif computerChoice == 2:
            print("Computer chose paper")
        elif computerChoice == 3:
            print("Computer chose scissors")

        # Check each possibility and output who won in each of these cases
        if userChoice == 1 and computerChoice == 2:
            print("The computer won")
        elif userChoice == 2 and computerChoice == 3:
            print("The computer won")
        elif userChoice == 3 and computerChoice == 1:
            print("The computer won")
        elif userChoice == 1 and computerChoice == 3:
            print("You won")
        elif userChoice == 2 and computerChoice == 1:
            print("You won")
        elif userChoice == 3 and computerChoice == 2:
            print("You won")
