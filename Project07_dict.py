birthdays = {"Jordy": "Dec 18", "Bo": "Nov 19", "Jordan": "Sep 12"}

while True:
    print("Enter a name: (black to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)

    else:
        print("I do not have information for" + name)
        print("What is your birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthdays database updated.")
        