file = open("./day3.txt", "r")
rows = file.readlines()
rows = [r.strip() for r in rows]
rows = [list(r) for r in rows]

treeCounter = 0
currentIndex = 0
#part 1, the currentIndex iterator can be remade for 4/5 of part 2
'''
for row in rows:
    print(row)
    if(currentIndex > 30):
        currentIndex = abs(31 - currentIndex)
        if(row[currentIndex] == "#"):
            print("yes: " + str(currentIndex))
            treeCounter = treeCounter + 1
    if(currentIndex <= 30):
        if(row[currentIndex] == "#"):
            print("yes: " + str(currentIndex))
            treeCounter = treeCounter + 1
    currentIndex = currentIndex + 3;

print(treeCounter)'''
            
#part 2
for i in range(0, len(rows), 2):
    print(rows[i])
    if(currentIndex > 30):
        currentIndex = abs(31 - currentIndex)
        '''if(row[currentIndex] == "#"):
            print("yes: " + str(currentIndex))
            treeCounter = treeCounter + 1'''
    if(currentIndex <= 30):
        if(rows[i][currentIndex] == "#"):
            print("yes: " + str(currentIndex))
            treeCounter = treeCounter + 1
    currentIndex = currentIndex + 1

print(treeCounter)
