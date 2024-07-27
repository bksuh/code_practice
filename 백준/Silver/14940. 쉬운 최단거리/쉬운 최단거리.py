import collections
n, m = map(int, input().split())
graph = []
dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]

def bfs(graph, x, y, visited):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = 0
    visited[x][y] = False
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny <0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny]:
                graph[nx][ny] = graph[x][y] +1
                visited[nx][ny] = False
                queue.append((nx, ny))

    return graph
for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        sx, sy = (i, tmp.index(2))
    graph.append(tmp)
visited = [[True]*m for _ in range(n)]
graph = bfs(graph, sx, sy, visited)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j]:
            graph[i][j] = -1
    print(*graph[i])