import random, sys

print("Rock and Paper")

wins = 0
losses = 0
ties = 0


while True: # The main game loop
    print("Win is " + str(wins))
    print("Losses is " + str(wins))
    print("Ties is " + str(wins))
    while True: # Player input loop.
        print("Enter your move: (r)ock (p)aper or (q)uit. q means leaving the game.")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        elif playerMove == "r" or playerMove == "p":
            break
        else:
            print("Type r OR p OR q.")

    # Display player's option.
    if playerMove == "r":
        print ("Rock versus ......")
    elif playerMove == "p":
        print("Paper versus......")

    # Rand computer's option.
    randomNumber = random.randint(1,2)
    if randomNumber == 1:
        computerMove = "r"
        print("Rock")
    else:
        computerMove = "p"
        print("Paper")
    
    # Print result
    if playerMove == computerMove:
        ties = ties + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1 

    

