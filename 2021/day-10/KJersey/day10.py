data = [line.strip() for line in open("day10.txt", 'r')]

stack = []
rows = []

counter = 0

for line in data:
    row = ''
    corrupt = False
    for c in line:
        if c in ['(', '[', '{', '<']:
            row += c
            stack.insert(0, c)
        elif c == ')' and stack.pop(0) != '(':
            corrupt = True
            counter += 3
            break
        elif c == ']' and stack.pop(0) != '[':
            corrupt = True
            counter += 57
            break
        elif c == '}' and stack.pop(0) != '{':
            corrupt = True
            counter += 1197
            break
        elif c == '>' and stack.pop(0) != '<':
            counter += 25137
            corrupt = True
            break
        else:
            row += c

    if not corrupt:
        rows.append(row)

print(counter)

scores = []

for row in rows:
    stack = []
    counter = 0
    for c in row:
        if c in ['(', '[', '{', '<']:
            stack.insert(0, c)
        else:
            stack.pop(0)
    for c in stack:
        if c == '(':
            counter *= 5
            counter += 1
        elif c == '[':
            counter *= 5
            counter += 2
        elif c == '{':
            counter *= 5
            counter += 3
        else:
            counter *= 5
            counter += 4

    scores.append(counter)

scores.sort()

print(scores[len(scores) // 2])