import collections
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(sx, sy, grid):
    queue = collections.deque()
    grid[sx][sy] = '.'
    queue.append((sx, sy))
    while queue:
        sx, sy = queue.popleft()
        for k in range(len(dx)):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if nx < 0 or nx >= n or ny< 0 or ny>=n:
                continue
            if grid[nx][ny] == '*':
                grid[nx][ny] = '.'
                queue.append((nx, ny))
                
    return grid

n = int(input())
grid =[]
cnt = 0
for _ in range(n):
    tmp = [c for c in input()]
    grid.append(tmp)
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            grid = bfs(i, j, grid)
            cnt += 1
print(cnt)