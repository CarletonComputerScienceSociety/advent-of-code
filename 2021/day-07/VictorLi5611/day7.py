data = [line.strip() for line in open("input.txt", 'r')]
for i, line in enumerate(data):
    words = line.split(",")
data = words

def part1(data):
    result = [int(i) for i in data]
    ans = float("inf")
    for i in range(min(result), max(result)):
        diff = sum(abs(i-j) for j in result)
        ans = min(ans, diff)
    print(ans)
    
    
def part2(data):
    result = [int(i) for i in data]
    ans = float("inf")
    for i in range(min(result), max(result)):
        diff = sum(abs(i-j) * (abs(i-j)+1)/2 for j in result)
        ans = min(ans, diff)
    print(ans)

part1(data)
part2(data)
