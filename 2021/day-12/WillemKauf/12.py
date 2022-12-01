from collections import defaultdict, deque

def read_input():
    input_map = defaultdict(list)
    with open("input/input12.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split("-")
            input_map[line[0]].append(line[1])
            if line[0] not in input_map[line[1]]:
                input_map[line[1]].append(line[0])
    return input_map

def part_1(input_map):
    queue = ["start"]
    def bfs(queue, seen):
        res = 0
        while len(queue):
            curr_node = queue.pop(0)
            if curr_node == "end":
                return 1
            for neighbour in input_map[curr_node]:
                if neighbour not in seen or neighbour.isupper():
                    res += bfs(queue+[neighbour], seen+[curr_node])
        return res
    return bfs(queue, [])

def part_2(input_map):
    def bfs(queue, unique_cave, seen):
        seen_paths = []
        while len(queue):
            curr_node = queue.pop(0)
            if curr_node == "end":
                return ["".join(seen+[curr_node])]
            for neighbour in input_map[curr_node]:
                if neighbour not in seen or (neighbour == unique_cave and seen.count(neighbour) < 2) or neighbour.isupper():
                    new_seen_paths = bfs(queue+[neighbour], unique_cave, seen+[curr_node])
                    for path in new_seen_paths:
                        seen_paths.append(path)
        return seen_paths

    res = 0
    seen_paths = []
    for unique_cave in [cave for cave in set(input_map) if cave not in ["start", "end"] and cave.islower()]:
        new_seen_paths = bfs(["start"], unique_cave, [])
        for path in new_seen_paths:
            if isinstance(path, list):
                for p in path:
                    seen_paths.append(p)
            else:
                seen_paths.append(path)
    return len(set(seen_paths))

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()
