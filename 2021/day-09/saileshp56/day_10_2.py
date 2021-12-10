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

def ending(row):
    d1 = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ending_row = []
    for item in row:
        ending_row.append(d1[item])

    return ending_row[::-1]



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
i = 0
to_remove = []
mylist2 = mylist[:]
while i < len(mylist):
    j = 0
    right_character = []
    left_character = ''
    while j < len(mylist[i]):

        if mylist[i][j] in right:
            right_character.append(mylist[i][j])

        elif mylist[i][j] in left:
            left_character = mylist[i][j]
            temp = sum
            sum += match(right_character[-1], left_character)
            if sum > temp:
                to_remove.append(i)
            right_character.pop()

        j += 1
    i += 1


for item in to_remove[::-1]:
    mylist2.pop(item)

endings = []
for row in mylist2:
    right_character = []
    left_character = ''

    for item in row:

        if item in right:
            right_character.append(item)

        elif item in left:
            left_character = item
            right_character.pop()
    endings.append(ending(right_character))


my_sums = []
mydict = {')': 1, ']': 2, '}': 3, '>': 4}
for row in endings:

    partial = 0
    for item in row:
        partial = partial * 5 + mydict[item]
    my_sums.append(partial)
my_sums.sort()
index = int(len(my_sums)/2)
print(my_sums[index])
