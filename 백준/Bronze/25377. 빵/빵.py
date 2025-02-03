import sys
n = int(input())
ans = sys.maxsize
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        ans = min(ans, b)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)