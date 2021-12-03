data = [line.strip() for line in open("input.txt", 'r')]

def p1(codes):
    length = len(codes[0])

    gamma = ""
    for i in range(length):
        column = "".join(code[i] for code in codes)
        if column.count("0") > column.count("1"):
            gamma += "0"
        else:
            gamma += "1"

    gamma = int(gamma, 2)
    eps = gamma ^ (pow(2, length) - 1)

    return gamma * eps

def p2(codes):

    length = len(codes[0])

    oxygen = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in oxygen)
        if column.count("0") <= column.count("1"):
            bit = "1"
        else:
            bit = "0"

        oxygen = oxygen - set(code for code in oxygen if code[i] == bit)
        if len(oxygen) == 1:
            oxygen = int(max(oxygen), 2)
            break

    co2 = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in co2)
        if column.count("0") > column.count("1"):
            bit = "1"
        else:
            bit = "0"

        co2 = co2 - set(code for code in co2 if code[i] == bit)
        if len(co2) == 1:
            co2 = int(max(co2), 2)
            break

    return oxygen * co2

print(p1(data))
print(p2(data))
