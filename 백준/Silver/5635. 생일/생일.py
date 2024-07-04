import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    name, d, m, y = input().rstrip().split()
    arr.append((name, int(y), int(m), int(d)))
arr.sort(key= lambda x : (-x[1], -x[2], -x[3]))
print(arr[0][0])
print(arr[-1][0])