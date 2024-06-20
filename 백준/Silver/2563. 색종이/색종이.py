grid = [[False]* 101 for _ in range(101)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            grid[i][j] = True
ans=0
for i in range(len(grid)):
    ans +=sum(grid[i])
print(ans)