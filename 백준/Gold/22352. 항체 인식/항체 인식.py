from collections import deque

n, m = map(int, input().split())
start_grid = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    start_grid.append(tmp)
result_grid = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    result_grid.append(tmp)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
def bfs(sx, sy, target):
    queue = deque()
    prev = start_grid[sx][sy]
    start_grid[sx][sy] = target
    queue.append((sx, sy))
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if nx < 0 or nx >= n or ny <0 or ny>=m:
                continue
            if start_grid[nx][ny] == prev:
                start_grid[nx][ny] = target
                queue.append((nx, ny))
    return start_grid
indi = False
for x in range(n):
    for y in range(m):
        if result_grid[x][y] != start_grid[x][y]:
            start_grid = bfs(x, y, result_grid[x][y])
            indi = True
            break
    if indi:
        break
    
print("YES" if start_grid == result_grid else "NO")