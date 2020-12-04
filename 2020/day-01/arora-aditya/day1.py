from collections import Counter
from helper.submit.submit import *
from utils import read_file_int

DAY = 1
setup(DAY)
file = read_file_int(DAY)

##################################################
counts = Counter(file)

ans = float('inf')
for num in counts:
    if 2020 - num in counts:
        ans = num * (2020 - num)
        break

submit(1, ans)

##################################################

ans = float('inf')
for i in counts:
    for j in counts:
        for k in counts:
            if i == j or i == k or j == k:
                continue
            if i + j + k == 2020:
                ans = i*j*k
                break

submit(2, ans)
