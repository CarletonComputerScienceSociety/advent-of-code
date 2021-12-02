def challenge1(nums):
    x = 0
    depth = 0
    for i in range(len(nums)):
        if nums[i].startswith("f"):
            x += int(nums[i][-1])
        elif nums[i].startswith("d"):
            depth += int(nums[i][-1])
        elif nums[i].startswith("u"):
            depth -= int(nums[i][-1])
    return x*depth


def challenge2(nums):
    x = 0
    depth = 0
    aim = 0
    for i in range(len(nums)):
        if nums[i].startswith("f"):
            x += int(nums[i][-1])
            depth += int(nums[i][-1])*aim
        elif nums[i].startswith("d"):
            aim += int(nums[i][-1])
        elif nums[i].startswith("u"):
            aim -= int(nums[i][-1])
    return x*depth

f = open("Day2.txt", 'r')
nums = []
for line in f:
    nums.append(line.strip())
f.close()
print(challenge2(nums))
