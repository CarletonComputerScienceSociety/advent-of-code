file = open("day10.txt")

chunkBrackets = {")": "(", "]": "[", "}": "{", ">": "<"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
syntaxErrorScore = 0

for line in file:
    stack = []
    for char in line.strip():
        if char in chunkBrackets.values():
            stack.append(char)
        elif char in chunkBrackets.keys():
            if chunkBrackets[char] != stack.pop():
                syntaxErrorScore += points[char]
                break
            
print(syntaxErrorScore)
