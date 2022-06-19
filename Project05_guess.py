import random
secretNumber = random.randint(1, 10)
print("I am thinking of a number between 1 and 20.")

for guessesTaken in range(1, 7):
    print("Make a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("You are right!, the secret number is " + str(secretNumber) + " .")
else:
    print("Nope, the number I was thinking of was " + str(secretNumber) + " .")

