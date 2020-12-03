f = open("day1In.txt","r")

nums = [int(i) for i in f.readlines()]
f.close()
nums.sort()
print(nums)
a=0
b=len(nums)-1
for i in range(len(nums)): 
  if nums[a] + nums[b] == 2020:
    break
  elif nums[a] + nums[b] < 2020:
    a += 1
  else:
    b -= 1

a = nums[a]
b = nums[b]
print(a,b,a+b,a*b)