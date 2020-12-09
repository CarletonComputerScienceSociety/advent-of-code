data = [int(line.strip()) for line in open("input.txt", 'r')]

#check the sum for each number in preamble
def two_sum(data, tar):
    dic = {}
    for num in data:
        if num in dic.keys():
            return num*dic[num]
        else:
            dic[tar-num] = num
    return False


def solve1(data):
    for i in range(25, len(data)):
        preamble = data[i-25:i]
        if not two_sum(preamble, data[i]):
            num = data[i]
            break
    return num

def solve2(data,num):
    for k in range(2, 50):
        for i in range(0, len(data)-k):
            curr_lst = []
            for j in range(0, k):
                curr_lst.append(data[i+j])
            if sum(curr_lst) == num:
                return min(curr_lst)+max(curr_lst)


print(solve1(data))
print(solve2(data,solve1(data)))
