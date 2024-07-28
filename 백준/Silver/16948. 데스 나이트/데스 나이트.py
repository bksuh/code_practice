import collections
n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
sx, sy, ex, ey = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
def bfs(graph, sx, sy, ex, ey):
    queue = collections.deque()
    queue.append((sx, sy))
    graph[sx][sy] = 1
    while queue:
        x, y = queue.popleft()
        if x== ex and y== ey:
            return graph[ex][ey] - 1
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx > n or ny > n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return -1
ans = bfs(graph, sx, sy, ex, ey)
print(ans)