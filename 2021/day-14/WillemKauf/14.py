from collections import Counter, defaultdict

def read_input():
    input_dct = {}
    with open("input/input14.txt") as input_file:
        input_mol = input_file.readline().rstrip()
        for line in input_file:
            line = line.rstrip()
            if line == "":
                pass
            else:
                line = line.split(" -> ")
                input_dct[line[0]] = line[1]
    return input_mol, input_dct

def part_1(input_mol, input_dct):
    for _ in range(0, 10):
        i = 0
        while i < len(input_mol)-1:
            mol_str = input_mol[i] + input_mol[i+1]
            if mol_str in input_dct:
                append_str = input_dct[mol_str]
                input_mol = input_mol[:i+1] + append_str + input_mol[i+1:]
                i += 1
            i += 1

    final_count = Counter(input_mol)
    return max(final_count.values()) - min(final_count.values())

def part_2(input_mol, input_dct):
    j = 0
    count_dct = Counter([input_mol[i]+input_mol[i+1] for i in range(0, len(input_mol)-1)])

    for _ in range(0, 40):
        new_count_dct = defaultdict(int)
        for pair, num in count_dct.items():
            append_str = input_dct[pair]
            new_count_dct[pair[0]+append_str[0]] += num
            new_count_dct[append_str[0]+pair[1]] += num
        count_dct = new_count_dct

    final_count_dct = defaultdict(int)
    for pair, num in count_dct.items():
        final_count_dct[pair[0]] += num
    final_count_dct[input_mol[-1]] += 1

    return max(final_count_dct.values()) - min(final_count_dct.values())

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()
