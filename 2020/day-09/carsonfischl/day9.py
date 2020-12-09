file = open("./day9.txt", mode="r")
lines = file.readlines()
numList = []

for line in lines:
    numList.append(int(line))
    
# part 1

# def check25(li):
#     for i in range(0, 25):
#         if i == 24: # throw if second last num is reached
#             print(li)
#             raise Exception
#         for j in range(i+1, 25):
#             if li[i] + li[j] == li[25]:
#                 print(li[25])
#                 print(i,j)
#                 print(li)
#                 return
# 
# k = 0
# while k <= len(numList):
#     thisList = numList[k:k+26]
#     try:
#         check25(thisList)
#         k += 1
#     except:
#         print(lines[k+25])
#         break

# part 2

i = 0
for i in range(0, 516): # line for my answer from part 1
    #print(numList[i])
    for j in range(i+1, 516):
        #print(numList[j])
        thisList = numList[i:j]
        thisMin = min(thisList)
        thisMax = max(thisList)
        if(sum(thisList) == 23278925): # my answer from part 1
            print(str(numList[i]) + " Index: " +  str(i))
            print(str(numList[j]) + " Index: " +  str(j))
            print("FOUND IT")
            print(thisMin + thisMax)
        else:
            continue