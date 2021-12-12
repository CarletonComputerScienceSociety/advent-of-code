from aoc import AOC

aoc = AOC(year=2021, day=8)
data = aoc.load()

# Part 1

displays = [l[0].strip().split(" ") for l in data.parse(r".*\|(.*)")]
unique = [2, 3, 4, 7]
aoc.p1(sum(sum(1 for d in display if len(d) in unique) for display in displays))

# Part 2

total_output = 0
for display in data.parse(r"(.*)\|(.*)"):
    signals, outputs = display
    signals = [set(x) for x in signals.strip().split(" ")]
    outputs = [set(x) for x in outputs.strip().split(" ")]

    # We can find signals 1, 4, 7, and 8 immediately
    for s in signals:
        if len(s) == 2:
            one = s
        elif len(s) == 3:
            seven = s
        elif len(s) == 4:
            four = s
        elif len(s) == 7:
            eight = s

    signals.remove(one)
    signals.remove(seven)
    signals.remove(four)
    signals.remove(eight)

    # Next, we find 0, 6, and 9
    six_len_signals = [s for s in signals if len(s) == 6]
    signals = [s for s in signals if s not in six_len_signals]

    for sx in six_len_signals:
        # Subtract segments for signals 4 and 7,
        # if there's exactly one segment remaining, the signal is 9
        if len(sx - (seven | four)) == 1:
            nine = sx
            six_len_signals.remove(nine)
            break

    # Next, remove the segments for 1, if 2 segments remain, we have 0
    zero = next(s for s in six_len_signals if len(s - one) == len(s) - 2)
    six_len_signals.remove(zero)

    # The last signal with 6 segments must be 6
    six = six_len_signals[0]

    # Finally, we find 2, 3, and 5
    five_len_signals = [s for s in signals if len(s) == 5]

    # If we subtract a signal from 6's segments, and have 1 segment remaining,
    # the signal must be 5
    five = next(s for s in five_len_signals if len(six - s) == 1)
    five_len_signals.remove(five)

    # The leftover segment must be E
    segment_e = list(six - five)[0]

    # Of the remaining signals, the one with segment E must be 2
    two = next(s for s in five_len_signals if segment_e in s)
    five_len_signals.remove(two)

    # The last signal is 3
    three = five_len_signals[0]

    output = 0
    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    for place, digit in zip(range(len(outputs) - 1, -1, -1), outputs):
        output += (10 ** place) * digits.index(digit)
    total_output += output

aoc.p2(total_output)

