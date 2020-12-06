file = open("day_6_input.txt", "r")
sumCount = 0
peopleInGroup = 0
currentGroup = ""
numCommonYes = 0

for line in file.readlines():
    if line == "\n":
        for char in set(currentGroup):
            if currentGroup.count(char) == peopleInGroup:
                numCommonYes += 1
        peopleInGroup = 0
        currentGroup = ""
    else:
        peopleInGroup += 1
        currentGroup += line.strip()

for char in set(currentGroup):
    if currentGroup.count(char) == peopleInGroup:
        numCommonYes += 1

print(numCommonYes)
