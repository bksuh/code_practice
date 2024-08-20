n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        if j == 0:
            grid[i][j] += grid[i-1][j]
        elif j == len(grid[i]) - 1:
            grid[i][j] += grid[i-1][j-1]
        else:
            grid[i][j] = max(grid[i][j]+grid[i-1][j-1], grid[i][j] + grid[i-1][j])
print(max(grid[len(grid)-1]))
