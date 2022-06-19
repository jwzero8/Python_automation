import sys

while True:
    print("Type exit to exit the program.")
    response = input()
    if response == "exit":
        sys.exit()
    else:
        print("You typed " + response + " as your response.")