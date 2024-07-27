import collections
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
l = int(input())

def bfs(grpah, x, y):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return graph

for _ in range(l):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            else:
                graph = bfs(graph, i, j)
                cnt +=1
    print(cnt)