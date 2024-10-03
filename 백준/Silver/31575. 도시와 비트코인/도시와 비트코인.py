n, m = map(int, input().split())
grid = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    grid.append(tmp)

from collections import deque

queue = deque()
dx, dy = [0, 1], [1, 0]
grid[0][0] = 2
queue.append((0, 0))
while queue:
    sx , sy = queue.popleft()
    for k in range(2):
        nx = sx + dx[k]
        ny = sy + dy[k]
        if nx < 0 or nx >=m or ny < 0 or ny >=n or grid[nx][ny]==0:
            continue
        if grid[nx][ny]==1:
            grid[nx][ny] = 2
            queue.append((nx,ny))

if grid[m-1][n-1] == 2:
    print('Yes')
else:
    print("No")