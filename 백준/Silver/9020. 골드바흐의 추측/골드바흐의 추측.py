t = 10000
arr = [i for i in range(t+1)]
for i in range(2, t+1):
    for j in range(2*i, t+1, i):
        arr[j]= 0

t = int(input())
for _ in range(t):
    x = int(input())
    tmp = []
    for i in range(2, x+1):
        if arr[i] == 0:
            continue
        if arr[x-i] != 0:
            tmp.append((i, x-i, abs(x-2*i)))
    tmp.sort(key=lambda x: (x[2], x[0]))
    print(tmp[0][0], tmp[0][1])
