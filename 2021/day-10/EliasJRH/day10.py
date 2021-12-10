import math

inf = """input"""

inf2 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

square = 0
round = 0
curly = 0
caret = 0

lines = [line for line in inf.split("\n")]

corrupt = []
toRemove = []

scores = {
    ')': 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

for count, line in enumerate(lines):
    stack = []
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            stack.append(char)
        elif char == ')':
            if stack[-1] == '(': stack.pop()
            else: 
                corrupt.append(')')
                toRemove.append(count)
                break
        elif char == ']':
            if stack[-1] == '[': stack.pop()
            else: 
                corrupt.append(']')
                toRemove.append(count)
                break
        elif char == '}':
            if stack[-1] == '{': stack.pop()
            else: 
                corrupt.append('}')
                toRemove.append(count)
                break   
        elif char == '>':
            if stack[-1] == '<': stack.pop()
            else: 
                corrupt.append('>')
                toRemove.append(count)
                break
sum = 0

for err in corrupt:
    sum += scores[err]

print(sum)

toRemove.reverse()

for x in range(len(lines) - 1, -1, -1):
    if x == toRemove[0]:
        del lines[x]
        del toRemove[0]
    
    if (len(toRemove) == 0):
        break

newSums = []

newScores = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

for count, line in enumerate(lines):
    stack = []
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            stack.append(char)
        elif char == ')':
            if stack[-1] == '(': stack.pop()
        elif char == ']':
            if stack[-1] == '[': stack.pop()
        elif char == '}':
            if stack[-1] == '{': stack.pop()
        elif char == '>':
            if stack[-1] == '<': stack.pop()
    
    stack.reverse()
    currSum = 0
    for char in stack:
        currSum *= 5
        currSum += newScores[char]
    
    newSums.append(currSum)

newSums.sort()


median = int(newSums[math.floor(len(newSums) / 2)]) #will always be an odd number of scores

print(median)
