
def findItem(bag):
    middle = (len(bag)-1)/2
    compartment1 = bag[0:int(middle)]
    compartment2 = bag[int(middle):]
    for char in compartment1:
        if compartment2.__contains__(char):
            if ord(char) >= 97:#lower case
                return ord(char) - 96
            else:#upper case
                return ord(char) - 38
    return 0

def part1():
    sum = 0
    file = open("input.txt")
    line = file.readline()
    while line != '':
        #find item and add priority
        sum += findItem(line)
        line = file.readline()
    return sum

def findBadge(group):
    for char in group[0]:
        if group[1].__contains__(char) and group[2].__contains__(char):
            if ord(char) >= 97:#lower case
                return ord(char) - 96
            else:#upper case
                return ord(char) - 38

def part2():
    sum = 0
    file = open('input.txt')
    line = file.readline()
    group = []
    while line != '':
        for i in range(0,3):
            group.append(line.strip('\n'))
            line = file.readline()
        sum += findBadge(group)
        group = []
    return sum

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()
