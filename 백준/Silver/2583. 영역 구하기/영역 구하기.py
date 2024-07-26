import collections

m, n, k = map(int, input().split())
graph = [[1]*(n) for _ in range(m)]
for _ in range(k):
    x, y, x1, y1 = map(int, input().split())
    for i in range(x, x1):
        for j in range(y, y1):
            graph[j][i] = 0

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1 
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >=m or ny >=n:
                continue
            if graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = 0
                cnt +=1

                queue.append((nx, ny))
    return graph, cnt

res = []

for i in range(n):
    for j in range(m):
        if graph[j][i] == 0:
            continue
        else:
            graph, ans = bfs(graph, j, i)
            res.append(ans)
res.sort()
print(len(res))
print(*res)
