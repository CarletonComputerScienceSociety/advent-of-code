day4 = __import__('Day-4-1')

STEPS = 2


def playFullGame(game):
    winners = []
    step = 0
    while len(game[1]) > 0:
        call = game[day4.CALLS][step]
        boardsToRevmove = []
        for i, board in enumerate(game[day4.BOARDS]):
            day4.playBoard(call, board)
            if day4.hasBoardWon(board):
                winners.append(board)
                board.append(step)
                boardsToRevmove.append(board)

        for board in boardsToRevmove:
            game[day4.BOARDS].remove(board)

        step += 1
    return winners


def main():
    input = open("input-4.txt", 'r')
    game = day4.readGame(input)
    input.close()

    winners = playFullGame(game)
    day4.printBoard(winners[0])
    day4.printBoard(winners[-1])
    print("score:", day4.getScore(winners[0]), "i:", winners[0][STEPS])
    print("score:", day4.getScore(winners[-1]), "i:", winners[-1][STEPS])


if __name__ == "__main__":
    main()
