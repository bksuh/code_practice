grid = [[0]*1001 for _ in range(1001)]
n = int(input())

for i in range(1, n+1):
    a, b, c, d = map(int, input().split())
    for x in range(a, a+c):
        for y in range(b, b+d):
            grid[x][y] = i
ans = [0 for _ in range(n+1)]
for i in range(len(grid)):
    for k in range(1, n+1):
        ans[k] +=grid[i].count(k)

for i in range(1, len(ans)):
    print(ans[i])