import pprint


message = "It has been four months since I returned to this country. I miss my friends in HK, the U.S. and Japan. Currently learning something new."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count) # This gives a ugly count for all the characters

"""To modify the program, use pprint to give formatted printing"""


pprint.pprint(count)