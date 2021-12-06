def read_input():
    input_lst = []
    with open("input/input6.txt") as input_file:
        for line in input_file:
            for c in line.rstrip().split(','):
                input_lst.append(int(c))
    return input_lst

def part_1(input_lst):
    for i in range(0, 80):
        hsh_map = {}
        counter = 0
        for i in range(0, len(input_lst)):
            input_lst[i] -= 1
            if input_lst[i] == -1:
                input_lst[i] = 6
                counter += 1
        for _ in range(0, counter):
            input_lst.append(8)
    return len(input_lst)

def part_2(input_lst):
    hsh_map = {}
    for num in set(input_lst):
        hsh_map[num] = input_lst.count(num)
    for i in range(0, 256):
        counter = 0
        new_hsh_map = {}
        for timer in hsh_map:
            if timer != 0:
                if timer-1 not in new_hsh_map:
                    new_hsh_map[timer-1] = hsh_map[timer]
                else:
                    new_hsh_map[timer-1] += hsh_map[timer]
            else:
                if 6 not in new_hsh_map:
                    new_hsh_map[6] = hsh_map[timer]
                else:
                    new_hsh_map[6] += hsh_map[timer]
                new_hsh_map[8] = hsh_map[timer]
        hsh_map = new_hsh_map
    return sum([v for v in hsh_map.values()])

def main():
    input_lst = read_input()
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
