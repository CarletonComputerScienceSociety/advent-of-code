def match(right, left):
    d1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    if right == '(' and left != ')':
        return d1[left]
    elif right == '[' and left != ']':
        return d1[left]
    elif right == '{' and left != '}':
        return d1[left]
    elif right == '<' and left != '>':
        return d1[left]
    else:
        return 0


f = open('input.txt', 'r')

file_data = f.read()

mys = file_data.strip().split('\n')
mylist = []
for line in mys:
    row = []
    for char in line:
        row.append(char)
    mylist.append(row)

incorrect_list = []
right = ['(', '[', '{', '<']
left = [')', ']', '}', '>']

sum = 0
for row in mylist:
    right_character = []
    left_character = ''
    for item in row:

        if item in right:
            right_character.append(item)

        elif item in left:
            left_character = item
            temp = sum
            sum += match(right_character[-1], left_character)

            right_character.pop()


print(sum)
