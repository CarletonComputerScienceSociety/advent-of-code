# part 1
file = open("day_10_input.txt", "r")

nums = [int(line.strip()) for line in file.readlines()]
diff = [0, 0, 0]
currentRating, count = 0, 0

while count < len(nums):
    count += 1
    for i in range(1, 4):
        if currentRating + i in nums:
            currentRating += i
            diff[i-1] += 1
            break

diff[2] += 1

print(diff[0] * diff[2])
