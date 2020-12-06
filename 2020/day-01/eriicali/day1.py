import itertools

file = open("day_1_input.txt", "r")
nums = [int(line.strip()) for line in file.readlines()]

allCombinations = itertools.combinations(nums, 3)

for combo in allCombinations:
    threeNums = tuple(combo)
    if threeNums[0] + threeNums[1] + threeNums[2] == 2020:
        print(threeNums[0] * threeNums[1] * threeNums[2])
        break
