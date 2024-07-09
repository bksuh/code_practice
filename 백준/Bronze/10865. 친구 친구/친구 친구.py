import sys

input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for i in range(n):
    d[i+1] = 0
for _ in range(m):
    a, b = map(int, input().split())
    d[a] +=1
    d[b] +=1
for elem in d.values():
    print(elem)