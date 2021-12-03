inf ="""input"""

inf2 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

nums = []

for line in inf2.split():
    nums.append(line)

ones = 0
zeroes = 0
most = ""
least = ""

# for x in range(len(nums[0])):
#     for count, line in enumerate(nums):
#         if nums[count][x] == "0":
#             zeroes += 1
#         else:
#             ones += 1
#     if (zeroes > ones):
#         most += "0"
#     else:
#         most += "1"
#     zeroes = 0
#     ones = 0
    
# for bit in most:
#     if bit == "0":
#         least += "1"
#     else:
#         least += "0"

# gamma = int (most, 2)
# epsilon = int (least, 2)

# print (gamma * epsilon)

ignoreindexes = set({})

for x in range(len(nums[0])):
    for count, line in enumerate(nums):
        if nums[count][x] == "0" and count not in ignoreindexes:
            zeroes += 1
        elif nums[count][x] == "1" and count not in ignoreindexes:
            ones += 1
    if (zeroes > ones):
        for count, line in enumerate(nums):
            if nums[count][x] == "1":
                ignoreindexes.add(count)
    else:
        for count, line in enumerate(nums):
            if nums[count][x] == "0":
                ignoreindexes.add(count)
    zeroes = 0
    ones = 0

ox = ""

for count, line in enumerate(nums):
        if count not in ignoreindexes:
            ox = line

ignoreindexes = set({})

for x in range(len(nums[0])):
    for count, line in enumerate(nums):
        if nums[count][x] == "0" and count not in ignoreindexes:
            zeroes += 1
        elif nums[count][x] == "1" and count not in ignoreindexes:
            ones += 1
    if (zeroes <= ones):
        for count, line in enumerate(nums):
            if nums[count][x] == "1":
                ignoreindexes.add(count)
    else:
        for count, line in enumerate(nums):
            if nums[count][x] == "0":
                ignoreindexes.add(count)
    if (len(ignoreindexes) == len(nums) - 1):
        break
    zeroes = 0
    ones = 0

co = ""

for count, line in enumerate(nums):
        if count not in ignoreindexes:
            co = line

ox = int(ox, 2)
co = int (co, 2)
print(ox * co)
