# part 2
nums = [int(num) for num in input.split(",")]
leastFuel = 100000000000
nums.sort()
upperBound = nums[-1]
print(upperBound)

for align in range(upperBound+1):
    fuel = 0
    for pos in nums:
        fuel += (abs(align - pos)*(abs(align - pos)+1))/2
    if fuel < leastFuel:
        leastFuel = fuel

print(leastFuel)
