with open('input.txt', 'r') as infile:
    data = [int(point) for point in infile.readlines()]

sums = []
window_tickers = [0, -1, -2, -3]
active_windows = [[] for _ in range(4)]
for i in range(len(data)):
    for j in range(len(active_windows)):
        if window_tickers[j] < 0:
            window_tickers[j] += 1
            continue
        if window_tickers[j] < 3:
            active_windows[j].append(data[i])
            window_tickers[j] += 1
        if len(active_windows[j]) == 3:
            sums.append(sum(active_windows[j]))
            active_windows[j] = []
            window_tickers[j] = 0

increases = 0
for index, point in enumerate(sums):
    if index == 0: continue
    if point > sums[index - 1]: increases += 1
print(increases)