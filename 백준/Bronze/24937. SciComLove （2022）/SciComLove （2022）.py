from collections import deque

s = deque([c for c in "SciComLove"])
n = int(input())
n %= 10
for _ in range(n):
    s.append(s.popleft())

print(''.join(s))