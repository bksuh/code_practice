import collections
arr = [i for i in range(10001)]
for i in range(len(arr)):
    v = i + sum([int(c) for c in str(i)])
    if v >= 10001:
        continue
    arr[v] = 0

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    else:
        print(i)