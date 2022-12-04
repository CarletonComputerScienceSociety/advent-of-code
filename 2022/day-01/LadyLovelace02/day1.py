def findLargest(array):
    largestSum = 0
    sum = 0
    for elf in array:
        for food in elf:
            sum += food
        if sum > largestSum:
            largestSum = sum
        sum = 0
    return largestSum

def remove(array, largest):
    sum = 0
    index = 0
    for elf in array:
        for food in elf:
            sum += food
        if sum == largest:
            array.pop(index)
            return
        sum = 0;
        index += 1

def main():
    elves = []
    elf = []
    #take input
    #read into array
    file = open('input.txt', 'r')
    line = file.readline()
    while line != '':#end of file
        line = file.readline()
        if line == '':
            break;
        elif line != '\n':
            line = line.strip('\n')
            elf.append(int(line))
        else:
            elves.append(elf)
            elf = []
    #find largest member
    print(elves)
    sum = 0
    for i in range(0,3):
        largest = findLargest(elves)
        remove(elves, largest)
        sum += largest
    #return value of largest memeber
    print(sum)

if __name__ == "__main__":
    main()
