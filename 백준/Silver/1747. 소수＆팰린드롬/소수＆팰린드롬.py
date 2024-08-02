import sys
input = sys.stdin.readline

t = 3000000
arr = [i for i in range(t+1)]

for i in range(2, int(pow(t, 1/2))+1):
    for j in range(2*i, t+1, i):
        arr[j]= 0
arr[1] = 0

n = int(input())
for i in range(n, len(arr)):
    tmp = str(i)
    if tmp == tmp[::-1] and arr[i] != 0:
        print(tmp)
        break