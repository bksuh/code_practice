import collections

n, m = map(int, input().split())
grid = []
visited = [[False]*n for _ in range(m)]
for _ in range(m):
    tmp = list(input())
    grid.append(tmp)
dx, dy = [1, 0, -1, 0], [0,-1, 0, 1]

def bfs(current, sx, sy):
    queue = collections.deque()
    visited[sx][sy] = True
    queue.append((sx, sy))
    cnt = 1
    while queue:
        x , y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            elif grid[nx][ny] == current:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return (current,cnt)        
ans_b, ans_w = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            color,count = bfs(grid[i][j], i, j)
            if color == 'B':
                ans_b += count**2
            else:
                ans_w += count **2
                
print(ans_w, ans_b)
