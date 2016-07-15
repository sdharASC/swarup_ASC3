'''
This is going to generate random movie titles
'''
import random

titleOpener = [
    "The Wrath of ",
    "Return of the ",
    "The ",
    "Attack From ",
    "Attack on the ",
    "Kingdom of the ",
    "Mega ",
    "Looking For ",
    "Fault in the ",
    "Abnormal ",
    "Rise of the "
]

adjectives = [
    "Stupid ",
    "Amazing ",
    "Weird ",
    "Deadly ",
    "Undead ",
    "Towering ",
    "Nimble ",
    "Narcissistic ",
    "Slippery ",
    "Wretched ",
    "Impolite "
]

nouns = [
    "AbreuBoom",
    "Spiders",
    "Dino",
    "Jim",
    "Terminator",
    "Ants",
    "Chickens",
    "Society",
    "Toad",
    "Witch",
    "Rat",
    "Jacky Chan"
]

# This takes a random string from each of the three lists
# returns a string which combines the three random words
def generateRandomMovie():
    first = titleOpener[random.randint(0, len(titleOpener) - 1)]
    second = adjectives[random.randint(0, len(adjectives) - 1)]
    last = nouns[random.randint(0, len(nouns) - 1)]
    return (first + second + last)

# print 10 random movie titles
for i in range(10):
    print(str(i+1)+". "+ generateRandomMovie())

