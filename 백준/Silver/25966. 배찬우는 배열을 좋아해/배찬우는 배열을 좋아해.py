import sys
input = sys.stdin.readline

grid = []
n, m, q = map(int, input().split())

grid = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    grid.append(tmp)

for _ in range(q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        _, i, j = arr
        grid[i], grid[j] = grid[j], grid[i]
    else:
        _, i, j, k = arr
        grid[i][j] = k

for elem in grid:
    print(*elem)
