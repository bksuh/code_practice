grid = []
for _ in range(9):
    arr = list(map(int, input().split()))
    grid.append(arr)
x, y, ans = 0,0, grid[0][0]
for i in range(9):
    for j in range(9):
        if grid[i][j] >= ans:
            x = i+1
            y = j+1
            ans = grid[i][j]
print(ans)
print(x, y)