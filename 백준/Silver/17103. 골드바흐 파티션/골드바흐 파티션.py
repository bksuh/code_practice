import sys
input = sys.stdin.readline

t = 1000000
arr = [i for i in range(t+1)]

for i in range(2, int(pow(t, 1/2))+1):
    for j in range(2*i, t+1, i):
        arr[j]= 0
arr[1] = 0

t = int(input())
for _ in range(t):
    x = int(input())
    tmp = []
    for i in range(2, int((x+1)/2) + 1):
        if arr[i] == 0:
            continue
        if arr[x-i] != 0:
            tmp.append((i, x-i))
    print(len(tmp))