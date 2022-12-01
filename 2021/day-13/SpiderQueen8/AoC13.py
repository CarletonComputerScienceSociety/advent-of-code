
def printPaper(dotSet):
    for i in range(6):
        row = ""
        for j in range(40):
            if (j, i) in dotSet:
                row += "#"
            else:
                row +=" "
        print(row)
    print()

def fold(dots, i):
    toAdd = []
    remove = []
    fold = int(i[1])
    if i[0] == 'y':
        for j in dots:
            if j[1] > fold:
                toAdd.append(((j[0], fold - (j[1] - fold))))
                remove.append((j[0], j[1]))
    if i[0] == 'x':
        for j in dots:
            if j[0] > fold:
                toAdd.append(((fold - (j[0] - fold), j[1])))
                remove.append((j[0], j[1]))
    for i in toAdd:
        dots.add(i)
    for i in remove:
        dots.remove(i)

def challenge1(dots, folds):
    dotSet = set(())
    for i in dots:
        dotSet.add((int(i[0]), int(i[1])))
    fold(dotSet, folds[0])
    return len(dotSet)

def challenge2(dots, folds):
    dotSet = set(())
    for i in dots:
        dotSet.add((int(i[0]), int(i[1])))
    for i in folds:
        fold(dotSet, i) 
    return dotSet

f = open("Input.txt", 'r')
dots = []
folds = []
gap = False
for line in f:
    if line == "\n":
        gap = True
    elif gap:
        folds.append(line.strip().split()[-1].split("="))
    else:
        dots.append(line.strip().split(","))
f.close()
print(challenge1(dots, folds))
printPaper(challenge2(dots, folds))
