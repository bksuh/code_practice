import collections

n, m = map(int, input().split())
graph = []
dx, dy = [1, 0, -1, 0],[0, -1, 0, 1]

for _ in range(n):
    tmp = list(int(c) for c in input())
    graph.append(tmp)

def bfs(graph, x, y):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = -1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
                queue.append((nx, ny))

for i in range(m):
    if graph[0][i] == 0:
        bfs(graph, 0, i)

if -1 in graph[n-1]:
    print("YES")
else:
    print("NO")