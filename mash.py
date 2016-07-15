'''
This is the 'mash' game
'''
import random

questions = [
    "What kind of house will you live in?",
    "Who will you marry?",
    "How many kids will you have?",
    "How many pets will you have?",
    "What color will be the house?",
    "Where will you live?"
]

houseStructure = ["Mansion", "Apartment", "Shack", "Rundown House"]
marry = ["Jenny", "???", "Abraham Lincoln", "Trump", "Donald Duck",
         "Superman", "A turnip", "A millionaire"]
colorOfHouse = ["black", "maroon", "yellow", "blood red", "sea green", "Luigi green"]
locations = ["USA", "Under a rock", "The moon", "France", "Mars", "A tree house"
             "Pirate ship"]
kids = [10, 0, -1, 12, 73]
pets = [25, 2, 0, 4, -2]
                          
userInput = []

for i in questions:
    userInput.append(raw_input(i))

houseStructure.append(userInput[0])
marry.append(userInput[1])
kids.append(userInput[2])
pets.append(userInput[3])
colorOfHouse.append(userInput[4])
locations.append(userInput[5])

h = houseStructure[random.randint(0, len(houseStructure) -1)]
m = marry[random.randint(0, len(marry) -1)]
c = colorOfHouse[random.randint(0, len(colorOfHouse)-1)]
l = locations[random.randint(0, len(locations)-1)]
p = pets[random.randint(0, len(pets) -1)]
k = kids[random.randint(0, len(kids) -1)]


fname = "C:\\Users\\Swarup Dhar\\Desktop\\test.txt"

with open(fname) as f:
    for line in f:
        print(line)
print("")

print("=====================")        
print(questions[0] + " " +h)
print(questions[1] + " " +m)
print(questions[2] + " " +str(k))
print(questions[3] + " " +str(p))
print(questions[4] + " " +c)
print(questions[5] + " " +l)
print("=====================")