inf = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

lines = [list(map(int, i)) for i in inf.split("\n")]



def solve():
    flashes = 0
    count = 0
    
    while(True):
        count += 1
        #first increment everything by one
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                lines[row][col] += 1

        tempFlashes = flashes

        tenFound = True
        while (tenFound):
            tenFound = False
            for row in range(len(lines)):
                for col in range(len(lines[row])):
                    if lines[row][col] >= 10:
                        tenFound = True
                        lines[row][col] = 0
                        flashes += 1
                        #up
                        if row - 1 >= 0 and int(lines[row - 1][col]) != 0:
                            lines[row - 1][col] += 1
                        #left
                        if col - 1 >= 0 and int(lines[row][col - 1]) != 0:
                            lines[row][col - 1] += 1
                        #down
                        if row + 1 < len(lines) and int(lines[row + 1][col]) != 0:
                            lines[row + 1][col] += 1
                        #right
                        if col + 1 < len(lines[row]) and int(lines[row][col + 1]) != 0:
                            lines[row][col + 1] += 1
                        #top left
                        if row - 1 >= 0 and col - 1 >= 0 and int(lines[row - 1][col - 1]) != 0:
                            lines[row - 1][col - 1] += 1
                        #top right
                        if row - 1 >= 0 and col + 1 < len(lines[row]) and int(lines[row - 1][col + 1]) != 0:
                            lines[row - 1][col + 1] += 1
                        #bottom left
                        if row + 1 < len(lines) and col - 1 >= 0 and int(lines[row + 1][col - 1]) != 0:
                            lines[row + 1][col - 1] += 1
                        #bottom right
                        if row + 1 < len(lines) and col + 1 < len(lines[row]) and int(lines[row + 1][col + 1]) != 0:
                            lines[row + 1][col + 1] += 1

        if (count == 100):
            print(flashes)

        if flashes - tempFlashes == 100:
            print(count)
            break                
        
solve()
