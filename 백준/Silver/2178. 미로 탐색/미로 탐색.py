from collections import deque
n, m = map(int, input().split())
graph = [list(int(c) for c in input()) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
check=[]

def bfs (graph, x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        cnt+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]
print(bfs(graph,0,0))

