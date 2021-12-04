data = [line.strip() for line in open("day4.txt", 'r')]

counter = 0
pos = [0, 0]

numbers = data[0].split(',')

boards = []

for i in range(1, len(data)):
    words = data[i].split()
    if(len(words) == 1 or len(words) == 0):
        continue
    board = words

    if counter % 5 == 0:
        boards.append([])

    boards[counter // 5].append(board)

    counter += 1
    


def findWinner(winners):
    for n in numbers:
        for board in boards:
            for i in range(len(board)):
                board[i] = list(map(lambda x: 'x' + n if x == n else x, board[i]))

        for board in boards:
            if board in winners:
                continue
            for row in board:
                win = True
                for i in range(len(row)):
                    if not row[i][0] == 'x':
                        win = False
                        break

                if win:
                    return board, int(n)

            for i in range(len(board[0])):
                win = True
                for j in range(len(board)):
                    if not board[j][i][0] == 'x':
                        win = False
                        break

                if win:
                    return board, int(n)

winners = []

while not len(winners) == len(boards):
    winner, num = findWinner(winners)
    winners.append(winner)

print(winner)

counter = 0

for row in winner:
    for n in row:
        if not n[0] == 'x':
            counter = counter + int(n)

print(counter * num)