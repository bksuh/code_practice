import sys
import collections
dx , dy = [1, 0, -1, 0], [0, -1, 0, 1]
def bfs(i, j):
    queue = collections.deque()
    sx, sy = i, j
    queue.append((sx, sy))
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= m or ny < 0 or ny >=n or visited[nx][ny]:
                continue
            elif grid[nx][ny] == 'T':
                queue.append((nx, ny))
                grid[nx][ny] =  'S'
                visited[nx][ny] = True
                
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    grid = []
    for _ in range(m):
        tmp = list(input())
        grid.append(tmp)
    
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                bfs(i, j)
    for elem in grid:
        print(*elem, sep='')