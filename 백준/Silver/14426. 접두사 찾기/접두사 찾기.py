import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
names = [input().rstrip() for _ in range(n)]
starts = [input().rstrip() for _ in range(m)]

names.sort()

cnt = 0
for start in starts:
    idx = bisect.bisect_left(names, start)
    if idx < n and names[idx].startswith(start):
        cnt += 1

print(cnt)
