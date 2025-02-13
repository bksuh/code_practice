import math

n, m = map(int, input().split())
cnt = 0

for _ in range(n):
    s = input()
    if s.count('O') >= math.ceil(m/2):
        cnt += 1

print(cnt)