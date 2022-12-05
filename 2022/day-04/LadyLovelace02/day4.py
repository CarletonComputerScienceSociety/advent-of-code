
def checkOverlap(array):
    if (int(array[0][0]) <= int(array[1][0]) and int(array[0][1]) >= int(array[1][1])) or (int(array[1][0]) <= int(array[0][0]) and int(array[1][1]) >= int(array[0][1])):
        return 1
    else:
        return 0

def part1():
    sum = 0
    file = open("input.txt")
    line = file.readline()
    while line != '':
        line = line.strip('\n')
        array = []
        elves = line.split(',')
        for elf in elves:
            array.append(elf.split('-'))
        sum += checkOverlap(array)
        line = file.readline()
    return sum

def checkOverlap2(array):
    if (int(array[0][0]) >= int(array[1][0]) and int(array[0][0]) <= int(array[1][1])) or (int(array[1][0]) >= int(array[0][0]) and int(array[1][0]) <= int(array[0][1])):
        return 1
    else:
        return 0

def part2():
    sum = 0
    file = open("input.txt")
    line = file.readline()
    while line != '':
        line = line.strip('\n')
        array = []
        elves = line.split(',')
        for elf in elves:
            array.append(elf.split('-'))
        sum += checkOverlap2(array)
        line = file.readline()
    return sum

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()
