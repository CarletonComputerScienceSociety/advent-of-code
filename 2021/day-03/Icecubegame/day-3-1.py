input = open("input-3.txt", 'r')

count = 0
bit_count = []

for bit in input.readline().strip():
    bit_count.append(int(bit))
count += 1

for line in input.readlines():
    bits = line.strip()
    count += 1
    for i, b in enumerate(bits):
        bit_count[i] += int(b)

gamma = ""
epsilon = ""

for c in bit_count:
    if c >= count/2:
        gamma += "1"
        epsilon += "0"
    elif c < count/2:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
