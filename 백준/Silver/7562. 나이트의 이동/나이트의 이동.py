import collections
n = int(input())
dx, dy = [1,2,2,1,-1,-2,-2,-1], [2, 1, -1, -2, -2, -1, 1 ,2]
def bfs(graph, sx, sy, ex, dy):
    queue = collections.deque()
    queue.append((sx, sy))
    graph[sx][sy] = 0
    while queue:
        x, y = queue.popleft()
        if ex == x and ey == y:
            break
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny <0 or nx >= t or ny >= t:
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for _ in range(n):
    t = int(input())
    graph = [[0]*t for _ in range(t)]

    sx, sy =map(int, input().split())
    ex, ey = map(int, input().split())

    bfs(graph, sx, sy, ex, dy)
    print(graph[ex][ey])