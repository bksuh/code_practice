import sys
input = sys.stdin.readline

t = int(input())

h, w = 0, 0

for _ in range(t):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)

    h, w = max(h, a), max(w, b)

print(h*w)