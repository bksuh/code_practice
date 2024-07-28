import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
queue = collections.deque()
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            queue.append((i, j))
    graph.append(tmp)

def bfs(graph, queue):
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(graph, queue)
ans = -1
indi = True
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            indi = False
        ans = max(ans, graph[i][j])
if indi:
    print(ans-1)
else:
    print(-1)