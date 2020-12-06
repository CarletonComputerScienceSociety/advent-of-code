def checkgroupanswers(a):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for letter in alph:
        found = True
        for answer in a:
            if not letter in answer:
                found = False
                break
        if found == True:
            count += 1
    return count
        

filein = open("day6.txt", "r")
file = filein.read()

groups = file.split("\n\n")
summ = 0
for group in groups:
    answers = group.split()
    summ += checkgroupanswers(answers)

print(summ)
