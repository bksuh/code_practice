import collections
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def bfs(sx, sy, grid):
    queue = collections.deque()
    grid[sx][sy] = '*'
    queue.append((sx, sy))
    while queue:
        sx, sy = queue.popleft()
        for k in range(len(dx)):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if nx < 0 or nx >= n or ny< 0 or ny>=m:
                continue
            if grid[nx][ny] == '@':
                grid[nx][ny] = '*'
                queue.append((nx, ny))
                
    return grid

while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    grid =[]
    cnt = 0
    for _ in range(n):
        tmp = [c for c in input()]
        grid.append(tmp)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                grid = bfs(i, j, grid)
                cnt += 1
    print(cnt)