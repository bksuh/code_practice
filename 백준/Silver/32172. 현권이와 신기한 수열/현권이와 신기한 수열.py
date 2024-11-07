t = int(input())
checker = [0 for _ in range(592217)]
arr = [0]
for i in range(1, t+1):
    tmp = arr[i-1] - i
    if tmp <= 0 or checker[tmp]==1:
        tmp = arr[i-1] + i
    checker[tmp] = 1
    arr.append(tmp)
print(arr[-1])
