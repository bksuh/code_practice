import sys
import collections
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = []
dx, dy, dz = [1, 0, -1, 0, 0, 0], [0, -1, 0, 1, 0, 0], [0, 0, 0, 0, 1, -1]

for _ in range(k):
    tmp = []
    for _ in range(m):
        ans = list(map(int, input().split()))
        tmp.append(ans)
    graph.append(tmp)

queue = collections.deque()

for z in range(k):
    for x in range(m):
        for y in range(n):
            if graph[z][x][y] == 1:
                queue.append((z, x, y))

if queue:
    while queue:
        z, x, y = queue.popleft()
        for t in range(6):
            nz = z + dz[t]
            nx = x + dx[t]
            ny = y + dy[t]
            if nz < 0 or nx < 0 or ny < 0 or nz >= k or nx >= m or ny >=n:
                continue
            if graph[nz][nx][ny] == -1 or graph[nz][nx][ny] == 1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

ans = graph[0][0][0]
for z in range(k):
    for x in range(m):
        for y in range(n):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            else:
                tmp = graph[z][x][y]
                ans = max(tmp, ans)
print(ans-1)
