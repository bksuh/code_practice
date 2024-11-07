import collections
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(sx, sy, grid):
    queue = collections.deque()
    grid[sx][sy] = '.'
    cnt = 1
    queue.append((sx, sy))
    while queue:
        sx, sy = queue.popleft()
        for k in range(len(dx)):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if nx < 0 or nx >= m or ny< 0 or ny>=n:
                continue
            if grid[nx][ny] == '*':
                grid[nx][ny] = '.'
                queue.append((nx, ny))
                cnt+=1
                
    return cnt

n, m = map(int, input().split())

grid =[]
ans = 0
for _ in range(m):
    tmp = [c for c in input()]
    grid.append(tmp)
for i in range(m):
    for j in range(n):
        if grid[i][j] == '*':
            ans = max(ans, bfs(i, j, grid))
print(ans)