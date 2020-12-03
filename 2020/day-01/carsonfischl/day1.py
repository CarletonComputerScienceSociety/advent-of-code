file = open("./day1.txt", "r")
numbers = file.readlines()
numbers = {int(line) for line in numbers}

numDict = dict.fromkeys(numbers, 0)
numDict2 = dict.fromkeys(numbers, 0)

for keey in numDict.keys():
    for numb in numbers:
        for numb3 in numbers:
            if (keey + numb + numb3) == 2020:
                numDict[keey] = int(numb)
                numDict2[keey] = int(numb3)

for numb2 in numDict.keys():
    if (int(numDict[numb2]) + int(numDict2[numb2]) + int(numb2)) == 2020:
        print( (numDict.get(numb2)) *numb2 * (numDict2.get(numb2)) )
        break