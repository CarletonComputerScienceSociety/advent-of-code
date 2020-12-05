f= open('inputday5.txt', 'r')
inp_string = f.read()
f.close()
inp_list = inp_string.split()

yours = 0
vals = []
for i in inp_list:
    top = 0
    bottom = 127
    middle = 0
    for j in range(0,6):
        middle = (top+bottom)/2
        if i[j] == 'B':
            top = middle + 1
        else:
            bottom = middle - 1
    if i[6] == 'F':
        middle = (top + bottom) // 2
    else:
        middle = -(-(top+bottom) // 2)

    mid = 0
    top = 0
    bottom = 7
    for j in range(7, 9):
        mid = (top+bottom)/2
        if i[j] == 'L':
            bottom = mid - 1
        else:
            top = mid + 1
    if i[9] == 'L':
        mid = (top + bottom) // 2
    else:
        mid = -(-(top + bottom) // 2)
    sid = middle*8 + mid
    vals.append(sid)

print(max(vals))

# PART 2

count = 0
vals = []
for i in inp_list:
    top = 0
    bottom = 127
    middle = 0
    for j in range(0,6):
        middle = (top+bottom)/2
        if i[j] == 'B':
            top = middle + 1
        else:
            bottom = middle - 1
    if i[6] == 'F':
        middle = (top + bottom) // 2
    else:
        middle = -(-(top+bottom) // 2)

    mid = 0
    top = 0
    bottom = 7
    for j in range(7, 9):
        mid = (top+bottom)/2
        if i[j] == 'L':
            bottom = mid - 1
        else:
            top = mid + 1
    if i[9] == 'L':
        mid = (top + bottom) // 2
    else:
        mid = -(-(top + bottom) // 2)
    sid = middle*8 + mid
    vals.append(sid)

    highest = max(vals)
    highest = int(highest)
    for val in range(0, highest):

        if (val - 1) in vals and (val + 1) in vals and val not in vals:
            yours = val
            break

print(yours)
