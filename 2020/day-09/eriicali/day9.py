import itertools

# part 1
preambleLength = 25
i = preambleLength
preambleStart = 0
hasPair = False
file = open("day_9_input.txt")
nums = [int(line.strip()) for line in file.readlines()]

while i < len(nums):
    hasPair = False
    for pair in itertools.combinations(nums[preambleStart:preambleStart+preambleLength], 2):
        currentPair = tuple(pair)
        if nums[i] == currentPair[0] + currentPair[1]:
            hasPair = True
    if not hasPair:
        print(nums[i])
        break
    i += 1
    preambleStart += 1
    
    
    
    
# part 2

total = 69316178
sumFound = False

file = open("day_9_input.txt")
nums = [int(line.strip()) for line in file.readlines()]

for i in range(len(nums)):
    if sumFound:
        break
    smallest = nums[i]
    largest = nums[i]
    j = i
    currentSum = 0
    while currentSum <= total:
        if nums[j] < smallest:
            smallest = nums[j]
        if nums[j] > largest:
            largest = nums[j]
        currentSum += nums[j]
        if currentSum == total:
            print(smallest + largest)
            sumFound = True
            break
        j += 1
