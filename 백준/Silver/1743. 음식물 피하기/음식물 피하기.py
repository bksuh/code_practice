import collections
n, m, t = map(int, input().split())
graph = [['.']*m for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(t):
    x, y = map(int, input().split())
    graph[x-1][y-1] = '#'
    
def bfs(grpah, x, y):
    queue = collections.deque()
    queue.append((x, y))
    cnt = 1
    graph[x][y] = "."
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            elif graph[nx][ny] == '#':
                cnt+=1
                graph[nx][ny] = '.'
                queue.append((nx, ny))
    return cnt

ans = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            tmp = bfs(graph, i, j)
            ans = max(ans, tmp)

print(ans)