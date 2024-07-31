import collections

n, m = map(int, input().split())
graph = []
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
def bfs(graph, x, y):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(graph, i, j)
            cnt += 1

print(cnt)