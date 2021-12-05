def read_input():
    input_lst = []
    with open("input/input5.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(" -> ")
            c1 = [int(p) for p in line[0].split(",")]
            c2 = [int(p) for p in line[1].split(",")]
            input_lst.append([c1, c2])
    return input_lst

def part_1(input_lst):
    hsh_dct = {}
    for line in input_lst:
        i_min = min(line[0][0], line[1][0])
        i_max = max(line[0][0], line[1][0])
        j_min = min(line[0][1], line[1][1])
        j_max = max(line[0][1], line[1][1])
        if j_min != j_max and i_min != i_max:
            continue
        for j in range(j_min, j_max+1):
            for i in range(i_min, i_max+1):
                coord = (i,j)
                if coord not in hsh_dct:
                    hsh_dct[coord] = 0
                hsh_dct[coord] += 1

    return sum([1 for k in hsh_dct.values() if k > 1])

def part_2(input_lst):
    hsh_dct = {}
    for line in input_lst:
        i_min = min(line[0][0], line[1][0])
        i_max = max(line[0][0], line[1][0])
        j_min = min(line[0][1], line[1][1])
        j_max = max(line[0][1], line[1][1])
        if j_min != j_max and i_min != i_max:
            i_1 = line[0][0]
            i_2 = line[1][0]
            j_1 = line[0][1]
            j_2 = line[1][1]

            if j_2 - j_1 < 0:
                my = -1
            else:
                my = 1

            if i_2 - i_1 < 0:
                mx = -1
            else:
                mx = 1

            for k in range(0, i_max-i_min+1):
                coord = (i_1+mx*k,j_1+my*k)
                if coord not in hsh_dct:
                    hsh_dct[coord] = 0
                hsh_dct[coord] += 1
        else:
            for j in range(j_min, j_max+1):
                for i in range(i_min, i_max+1):
                    coord = (i,j)
                    if coord not in hsh_dct:
                        hsh_dct[coord] = 0
                    hsh_dct[coord] += 1

    return sum([1 for k in hsh_dct.values() if k > 1])

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()

