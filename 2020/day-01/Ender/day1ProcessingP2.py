f = open("day1In.txt","r")

nums = [int(i) for i in f.readlines()]
f.close()
nums.sort()
print(nums)
a=0
b=0
c=0
foundFlag = False
#The bright side of this BS is that if it crashes, you know you didn't find it!
for i in range(len(nums)-2):       
  for j in range(i+1,len(nums)-1):
    for k in range(j+1,len(nums)):
      if nums[i] + nums[j] + nums[k] == 2020:
        foundFlag = True
        a = i
        b = j 
        c = k
        break
    if foundFlag:
      break
  if foundFlag:
    break

a = nums[a]
b = nums[b]
c = nums[c]
print(a,b,c,a+b+c,a*b*c)