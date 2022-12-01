
def challenge1(nums):
    fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in nums:
        fish[i] += 1
    for i in range(81):
        toApp = fish[0]
        for j in range(8):
            fish[j] = fish[j+1]
        fish[6] += toApp
        fish[8] = toApp
    counter = 0
    for i in range(8):
        counter += fish[i]
    return counter


def challenge2(nums):
    fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in nums:
        fish[i] += 1
    for i in range(257):
        toApp = fish[0]
        for j in range(8):
            fish[j] = fish[j+1]
        fish[6] += toApp
        fish[8] = toApp
    counter = 0
    for i in range(8):
        counter += fish[i]
    return counter

f = open("Input.txt", 'r')
nums = []
for line in f:
    nums = line.strip().split(",")
f.close()
nums = [int(num) for num in nums]
print(challenge1(nums))
print(challenge2(nums))
