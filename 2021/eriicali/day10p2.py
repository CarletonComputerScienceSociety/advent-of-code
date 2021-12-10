file = open("day10.txt")

chunkBrackets = {")": "(", "]": "[", "}": "{", ">": "<"}
chunkBracketsReverse = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []

for line in file:
    incomplete = True
    stack = []
    for char in line.strip():
        if char in chunkBrackets.values():
            stack.append(char)
        elif char in chunkBrackets.keys():
            if chunkBrackets[char] != stack.pop():
                incomplete = False
    if incomplete:
        completionScore = 0
        completionStr = ""
        while len(stack) > 0:
            completionStr += chunkBracketsReverse[stack.pop()]
        for brace in completionStr:
            completionScore *= 5
            completionScore += points[brace]
        scores.append(completionScore)

scores.sort()
print(scores[len(scores)//2])
