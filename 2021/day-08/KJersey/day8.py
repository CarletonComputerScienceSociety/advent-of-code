data = [line.strip() for line in open("day8.txt", 'r')]

counter = 0
for line in data:
    words = line.split(" ")[-4:]

    for word in words:
        if len(word) in [2, 3, 4, 7]:
            counter += 1

print(counter)

counter = 0
for line in data:
    words = sorted(line.split(" ")[:10], key=len)

    right = []

    for c in words[1]:
        if not c in words[0]:
            top = c
        else:
            right.append(c)

    for c in words[2]:
        if c in words[3] and c in words[4] and c in words[5]:
            middle = c

    for word in words:
        if len(word) == 5 and right[0] in word and right[1] in word and middle in word:
            for c in word:
                if c != top and c != right[0] and c != right[1] and c != middle:
                    bottom = c
    
    for c in words[9]:
        if c != top and not c in right and c != middle and c != bottom:
            if c in words[2]:
                topleft = c
            else:
                bottomleft = c

    if topleft in words[3]:
        if right[0] in words[3]:
            bottomright = right[0]
            topright = right[1]
        else:
            bottomright = right[1]
            topright = right[0]
    elif topleft in words[4]:
        if right[0] in words[4]:
            bottomright = right[0]
            topright = right[1]
        else:
            bottomright = right[1]
            topright = right[0]
    elif topleft in words[5]:
        if right[0] in words[5]:
            bottomright = right[0]
            topright = right[1]
        else:
            bottomright = right[1]
            topright = right[0]

    words = line.split(" ")[-4:]
    words.reverse()
    n = 0
    for c, w in enumerate(words):
        if top in w and topleft in w and topright in w and not middle in w and bottomleft in w and bottomright in w and bottom in w:
            n += 0 * pow(10, c)
        elif not top in w and not topleft in w and topright in w and not middle in w and not bottomleft in w and bottomright in w and not bottom in w:
            n += 1 * pow(10, c)
        elif top in w and not topleft in w and topright in w and middle in w and bottomleft in w and not bottomright in w and bottom in w:
            n += 2 * pow(10, c)
        elif top in w and not topleft in w and topright in w and middle in w and not bottomleft in w and bottomright in w and bottom in w:
            n += 3 * pow(10, c)
        elif not top in w and topleft in w and topright in w and middle in w and not bottomleft in w and bottomright in w and not bottom in w:
            n += 4 * pow(10, c)
        elif top in w and topleft in w and not topright in w and middle in w and not bottomleft in w and bottomright in w and bottom in w:
            n += 5 * pow(10, c)
        elif top in w and topleft in w and not topright in w and middle in w and bottomleft in w and bottomright in w and bottom in w:
            n += 6 * pow(10, c)
        elif top in w and not topleft in w and topright in w and not middle in w and not bottomleft in w and bottomright in w and not bottom in w:
            n += 7 * pow(10, c)
        if top in w and topleft in w and topright in w and middle in w and bottomleft in w and bottomright in w and bottom in w:
            n += 8 * pow(10, c)
        if top in w and topleft in w and topright in w and middle in w and not bottomleft in w and bottomright in w and bottom in w:
            n += 9 * pow(10, c)

    counter += n

print(counter)