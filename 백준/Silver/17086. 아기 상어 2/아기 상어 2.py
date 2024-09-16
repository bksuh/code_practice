import sys
import collections
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
queue = collections.deque()

for i in range(n):
    tmp = list(map(int, input().split()))
    grid.append(tmp)
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            visited[i][j] = True
        else:
            grid[i][j] = sys.maxsize
dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]
def bfs(visited_tmp, i, j):
    queue = collections.deque()
    queue.append((i,j))
    grid[i][j] = 0
    visited_tmp[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(len(dx)):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >=n or ny<0 or ny>=m or visited_tmp[nx][ny]:
                continue
            else:
                grid[nx][ny] = min(grid[nx][ny], grid[x][y]+1)
                visited_tmp[nx][ny] = True
                queue.append((nx, ny))

            
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            visited_tmp = copy.deepcopy(visited)
            bfs(visited_tmp, i, j)

tmp = -sys.maxsize

for elem in grid:
    tmp = max(tmp, max(elem))
print(tmp)