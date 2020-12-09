import string
from collections import Counter

file = open("./day6.txt", mode="r")
rows = file.read()
rows = list(rows.split('\n\n'))

rowDict = dict.fromkeys(string.ascii_lowercase, 0)
rowList = []
for row in rows:
    row = row.split('\n')
    rowList.append(row)

for group in rowList:
    thisGroup = Counter(string.ascii_lowercase)
    for passenger in group:
        thisGroup &= Counter(passenger)
    print(thisGroup)
    print(len(thisGroup))
    print(len(group))

    for letter in thisGroup.keys():
        rowDict[letter] += 1

print(sum(rowDict.values()))
print(rowDict)
