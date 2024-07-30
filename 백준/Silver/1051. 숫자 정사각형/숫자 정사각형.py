n, m = map(int, input().split())
tar = min(n,m)
grid = []
for _ in range(n):
    tmp = [int(c) for c in input()]
    grid.append(tmp)
if tar == 1:
    print(1)
else:
    ans = 1
    for t in range(1, tar):
        for i in range(n-t):
            for j in range(m-t):
                if grid[i][j] == grid[i+t][j+t] == grid[i+t][j] == grid[i][j+t]:
                    ans = max(ans, pow(t+1, 2))
    print(ans)