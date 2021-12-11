
points1 = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
points2 = {")" : 1, "]" : 2, "}" : 3, ">" : 4}

def checkComplete(line):
    open = []
    close = []
    points = 0
    for i in line:
        if i == '(' or i == '[' or i == '{' or i == '<':
            open.append(i)
        else:
            open.pop()
    for i in open:
        if i == "(":
            close.append(")")
        elif i == "[":
            close.append("]")
        elif i == "{":
            close.append("}")
        elif i == "<":
            close.append(">")
    close.reverse()
    for i in close:
        points *= 5
        points += points2[i]
    #print(close, points)
    return points

def checkCorrupted(line):
    open = []
    for i in line:
        if i == "(" or i == "[" or i == "{" or i == "<":
            open.append(i)
        else:
            if i == ")":
                if open[-1] == "(":
                    open.pop()
                else:
                    return points1[i]
            elif i == "]":
                if open[-1] == "[":
                    open.pop()
                else:
                    return points1[i]
            elif i == "}":
                if open[-1] == "{":
                    open.pop()
                else:
                    return points1[i]
            elif i == ">":
                if open[-1] == "<":
                    open.pop()
                else:
                    return points1[i]
    return 0

def challenge1(nums):
    counter = 0
    for i in nums:
        counter += checkCorrupted(i)
    return counter


def challenge2(nums):
    remove = []
    scores = []
    for i in nums:
        if checkCorrupted(i) != 0:
            remove.append(i)
    for i in remove:
        nums.remove(i)
    for i in nums:
        scores.append(checkComplete(i))
    scores.sort()
    return scores[round(len(scores)/2)]

f = open("Input.txt", 'r')
nums = []
for line in f:
    nums.append(line.strip())
f.close()
print(challenge1(nums))
print(challenge2(nums))
