import re

CALLS = 0
BOARDS = 1

ROWS = 0
CALLED = 1

NUM_ROWS = 5
NUM_COLUMNS = 5


def readCalledNumbers(input):
    numbers_string = input.readline()
    numbers_string = numbers_string.split(',')
    numbers = []
    for n in numbers_string:
        numbers.append(int(n))
    return numbers


def readRow(input):
    row_string = input.readline()
    row_string = re.split(" +", row_string.strip())
    row = []
    for n in row_string:
        row.append(int(n))
    return row


def readBoard(input):
    rows = []
    called = []

    for i in range(NUM_ROWS):
        rows.append([])

    for y in range(NUM_ROWS):
        row = readRow(input)
        rows[y] = row

    board = [rows, called]
    return board


def readGame(input):
    calls = readCalledNumbers(input)
    boards = []
    while input.readline() == "\n":
        boards.append(readBoard(input))
    return [calls, boards]


def printBoard(board):
    for row in board[ROWS]:
        print("{: >8} {: >8} {: >8} {: >8} {: >8}".format(*row))
    print(board[CALLED])


def printGame(game):
    print(game[CALLS])
    for board in game[BOARDS]:
        printBoard(board)


def hasRowWon(rows):
    hasWon = False
    for row in rows:
        count = 0
        for n in row:
            if type(n) == int:
                break
            count += 1
        if count == NUM_ROWS:
            hasWon = True
            break
    return hasWon


def hasColumnWon(rows):
    hasWon = False
    for y in range(NUM_COLUMNS):
        count = 0
        for row in rows:
            if type(row[y]) == int:
                break
            count += 1
        if count == NUM_COLUMNS:
            hasWon = True
            break
    return hasWon


def hasBoardWon(board):
    hasWon = hasRowWon(board[ROWS]) or hasColumnWon(board[ROWS])
    return hasWon


def playBoard(call, board):
    hasMatch = False

    y = 0
    while not hasMatch and y < len(board[0]):
        row = board[0][y]
        for x, num in enumerate(row):
            if num == call:
                row[x] = "check"
                hasMatch = True
                board[CALLED].append(call)
                break
        y += 1


def getScore(board):
    nonMatchSum = 0
    for row in board[0]:
        for n in row:
            if type(n) == int:
                nonMatchSum += n

    called = board[CALLED][-1]
    return nonMatchSum*called


def playGameUntilWinner(game):
    hasWinner = False
    winner = None
    i = 0
    while not hasWinner and i < len(game[0]):
        call = game[0][i]
        for board in game[BOARDS]:
            playBoard(call, board)
            if hasBoardWon(board):
                hasWinner = True
                winner = board
                break
        i += 1
    return winner


def main():
    input = open("input-4.txt", 'r')
    game = readGame(input)
    input.close()

    winner = playGameUntilWinner(game)
    printBoard(winner)
    print(getScore(winner))


if __name__ == "__main__":
    main()
