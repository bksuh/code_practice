import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ans = list(i for i in range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    tmp = ans[a-1:b]
    tmp.reverse()
    ans[a-1:b] = tmp
print(*ans)