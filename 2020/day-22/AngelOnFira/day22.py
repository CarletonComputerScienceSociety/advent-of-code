data = [line.strip() for line in open("input.txt", 'r')]

count = 0

seen = []

player_1 = []
for i, value in enumerate(data[1:26]):
    player_1.append(int(value))

player_2 = []
for i, value in enumerate(data[28:53]):
    player_2.append(int(value))


def play(player_1, player_2):
    this_game_seen = set()
    while len(player_1) > 0 and len(player_2) > 0:
        player_1_seen = "".join([str(x) + "," for x in player_1])
        player_2_seen = "".join([str(x) + "," for x in player_2])

        if player_1_seen in this_game_seen or player_2_seen in this_game_seen:
            return (1, player_1)
        this_game_seen.add(player_1_seen)
        this_game_seen.add(player_2_seen)

        winner = 0
        c1 = player_1.pop(0)
        c2 = player_2.pop(0)

        if c1 <= len(player_1) and c2 <= len(player_2):
            copy1 = [x for x in player_1[:c1]]
            copy2 = [x for x in player_2[:c2]]
            winner, score = play(copy1, copy2)

            if winner == 1:
                player_1.append(c1)
                player_1.append(c2)
            if winner == 2:
                player_2.append(c2)
                player_2.append(c1)

            continue

        if c1 > c2:
            player_1.append(c1)
            player_1.append(c2)
        if c2 > c1:
            player_2.append(c2)
            player_2.append(c1)

    if len(player_1) == 0:
        return (2, player_2)
    else:
        return (1, player_1)


winner, score = play(player_1, player_2)

for i, card in enumerate(score):
    count += card * (len(player_1) - i)

print(count)
