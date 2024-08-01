from collections import deque

def bfs(y, x, K):
    q.append((y, x))
    n = graph[y][x]
    visited[y][x] = 1
    graph[y][x] = K
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < R) and (0 <= X < C) and graph[Y][X] == n and not visited[Y][X]:
                graph[Y][X] = K
                visited[Y][X] = 1 
                q.append((Y, X))
                

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
Y, X, K = map(int, input().split())

visited = [[0] * C for _ in range(R)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()
bfs(Y, X, str(K))
for line in graph:
    print(''.join(line))