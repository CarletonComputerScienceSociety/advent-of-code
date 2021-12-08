import math
inf = """input"""

inf2 = """16,1,2,0,4,2,7,1,2,14"""

nums = [int(num) for num in inf2.split(",")]

nums.sort()

# print(nums)
# print(max(nums))
def solvept1(nums):
    if len(nums) % 2 == 0:
        median = int((nums[int(len(nums) / 2)] + nums[int((len(nums) / 2) - 1)]) / 2) 
    else: 
        median = int(nums[math.ceil(len(nums) / 2)])

    sum = 0
    for num in nums:
        sum += abs(num - median)

    print(sum)

def solvept2(nums):
    least = 0
    # leastx = 0

    for x in range(max(nums) + 1):
        # print(x)
        sum = 0
        for num in nums:
            n = abs(num - x)
            sum += int((pow(n, 2) + n) / 2)
        if (least == 0 or sum < least):
            # leastx = x
            least = sum

    # print(least, leastx)
    print(least)

solvept1(nums)
solvept2(nums)
