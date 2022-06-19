while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age")

while True:
    print("Type a password consisted of letters and numbers only:")
    password = input()
    if password.isalnum(): # .isalnum() returns True if the input is made up of alphabets and numbers only
        print("Password updated.")
        break
    print("Passwords can only have letters and numbers.")
