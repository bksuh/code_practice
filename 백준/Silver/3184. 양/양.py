from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total_wolf, total_sheep = 0, 0

visited = [[False]*(m) for _ in range(n)]

grid = []
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == '#':
            visited[i][j] = True
    grid.append(tmp)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def bfs(sx, sy):
    global total_sheep
    global total_wolf
    sheep, wolf = 0, 0
    queue = deque()
    queue.append((sx, sy))
    if grid[sx][sy] == 'v':
        wolf += 1
    elif grid[sx][sy] == 'o':
        sheep += 1
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny <0 or ny>=m or visited[nx][ny]:
                continue
            elif grid[nx][ny] == 'v':
                wolf += 1
            elif grid[nx][ny] == 'o':
                sheep += 1
            visited[nx][ny] = True
            queue.append((nx, ny))
    if wolf < sheep:
        total_sheep += sheep
    else:
        total_wolf += wolf
            
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        else:
            bfs(i,j)

print(total_sheep, total_wolf)