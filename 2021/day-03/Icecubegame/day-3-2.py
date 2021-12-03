def filter(report, condition):
    current_report = report.copy()
    length = len(current_report[0])
    i = 0

    while (len(current_report) > 1) and (i < length):
        count = len(current_report)
        bit_count = countBits(i, current_report)
        if bit_count != count and bit_count != 0:
            if (condition(bit_count, count/2)):
                current_report = current_report[0:bit_count]
            else:
                current_report = current_report[bit_count:]
        i += 1
    return current_report[0]


def countBits(i, report):
    count = 0
    for line in report:
        count += int(line[i])
    return count


def getOxygenGeneratorRating(report):
    return filter(report, lambda x, y: x >= y)


def getCO2ScrubberRating(report):
    return filter(report, lambda x, y: x < y)


input = open("input-3.txt", 'r')

report = [x.strip() for x in input.readlines()]
report.sort(reverse=True)


oxyRate = int(getOxygenGeneratorRating(report), 2)
scrubberRate = int(getCO2ScrubberRating(report), 2)

print(oxyRate * scrubberRate)
