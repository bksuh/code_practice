import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = int(input())
    arr = []
    for _ in range(t):
        a, b = input().rstrip().split()
        arr.append((int(a), b))
    arr.sort(key= lambda x: -x[0])
    print(arr[0][1])