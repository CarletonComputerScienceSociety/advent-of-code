def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

def fibb(n):
    i = 1
    gas = 0
    while i <= n:
        gas += i
        i += 1
    return gas





f = open('mymapdesert.txt', 'r')

file_data = f.read()

list_data = file_data.strip().split(',')
print(list_data)
int_list = []
for item in list_data:
    int_list.append(int(item))

pos = 0


temp = 10000000000000
for pos in range(max(int_list)):
    sum = 0
    for element in int_list:

        sum += fibb(abs(element - pos))

    if sum < temp:

        temp = sum
print(temp)
