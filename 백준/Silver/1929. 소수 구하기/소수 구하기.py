n, m = map(int, input().split())
arr = [i for i in range(m+1)]
arr[1] = 0
for i in range(2, m+1):
    if arr[i] == 0:
        continue
    for j in range(2*i, m+1, i):
        arr[j] = 0
for i in range(n, m+1):
    if arr[i] !=0:
        print(arr[i])
