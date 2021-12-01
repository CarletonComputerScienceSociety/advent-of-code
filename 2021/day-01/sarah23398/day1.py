import csv
arr = []
with open('input.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        arr.append(int(row[0]))

count = 0
for i in range(0, len(arr) - 1):
    if arr[i] < arr[i + 1]:
        count += 1

print(count)

count = 0
for i in range(0, len(arr) - 3):
    j = i + 1
    k = i + 2
    if (arr[i] + arr[j] + arr[k] < arr[i + 1] + arr[j + 1] + arr[k + 1]):
        count += 1

print (count)
