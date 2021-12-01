#A = (1 + 2 + 3)
#B = (2 + 3 + 4)
# B - A = (4 - 1)

# A < B --> 1 < 4

input = list(map(lambda x: int(x), open("input-1.txt", 'r').readlines()))
window = 3

count = 0

for i in range(0, len(input) - window):
    previous = input[i]
    current = input[i + 3]
    if previous < current:
        count += 1
print(count)
