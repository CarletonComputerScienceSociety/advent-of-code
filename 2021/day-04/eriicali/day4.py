# part 1

file = open("day4.txt")

draws = [num for num in file.readline().strip().split(",")]

lines = file.readlines()[1:]
lines = [line.strip() for line in lines if line != "\n"]
stop = False
boards = []
winningBoard = []
winningDraw = 0
i = 0
numWins = 0

while i < len(lines):
    board = [[num for num in line.split(" ") if num != ""] for line in lines[i:i+5]]
    boards.append(board)
    i += 5

print(boards)

for draw in draws:
    if stop == True:
        break
    for board in boards:
        if stop == True:
            break
        for row in board:
            if stop == True:
                break
            for col in range(5):
                if stop == True:
                    break
                if row[col] == draw:
                    row[col] = "X"
                    if row == ["X", "X", "X", "X", "X"] or board[0:5][col] == ["X", "X", "X", "X", "X"]:
                        winningBoard = board
                        winningDraw = int(draw)
                        stop = True
                    
sumUnmarked = 0
for row in winningBoard:
    for num in row:
        if num != "X":
            sumUnmarked += int(num)

print(sumUnmarked * winningDraw)

