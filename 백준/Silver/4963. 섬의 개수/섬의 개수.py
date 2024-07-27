import collections
dx = [0, 0, -1, 1,-1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]
def bfs(graph, x, y):
    queue = collections.deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >=m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return graph

while True:
    n, m = map(int, input().split())
    if n == 0 and m==0:
        break
    graph = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
    
    cnt = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            else:
                graph = bfs(graph, i, j)
                cnt += 1
    print(cnt)
            