from aoc import AOC, chunk, flatten, transpose

aoc = AOC(year=2021, day=4)
data = aoc.load()

finished_line = [None] * 5
numbers_drawn = data.numbers_by_line()[0]
bingo_cards = chunk(5, list(filter(None, data.numbers_by_line()[1:])))

# Part 1

# Check if a card has any finished rows or columns
def is_bingo(card):
    cols = transpose(card)
    return any(row == finished_line for row in card) or any(
        col == finished_line for col in cols
    )


for n in numbers_drawn:
    bingo_cards = [
        [[b[r][c] if b[r][c] != n else None for c in range(5)] for r in range(5)]
        for b in bingo_cards
    ]
    finished_cards = list(filter(is_bingo, bingo_cards))

    if finished_cards:
        last_drawn = n
        bingo = finished_cards[0]
        break

unmarked = sum(filter(None, flatten(bingo)))
aoc.p1(unmarked * last_drawn)

# Part 2

bingo_cards = chunk(5, list(filter(None, data.numbers_by_line()[1:])))

for n in numbers_drawn:
    bingo_cards = [
        [[b[r][c] if b[r][c] != n else None for c in range(5)] for r in range(5)]
        for b in bingo_cards
    ]
    unfinished_cards = list(filter(lambda x: not is_bingo(x), bingo_cards))

    if len(bingo_cards) == 1 and len(unfinished_cards) == 0:
        last_drawn = n
        bingo = bingo_cards[0]
        break

    bingo_cards = unfinished_cards

unmarked = sum(filter(None, flatten(bingo)))
aoc.p2(unmarked * last_drawn)

