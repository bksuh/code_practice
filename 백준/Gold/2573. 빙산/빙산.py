import collections

n, m = map(int, input().split())
graph = []
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
cnt = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    for k in tmp:
        if k != 0:
            cnt+=1
    graph.append(tmp)

def bfs(i, j):
    next = 0
    queue = collections.deque()
    queue.append((i, j))
    visited = [[-1]*m for _ in range(n)]
    visited[i][j] = 1
    real = 1
    water = 0
    for p in range(4):
        px = i + dx[p]
        py = j + dy[p]
        if px < 0 or py < 0 or px >=n or py >=m:
            continue
        if graph[px][py] == 0:
            water +=1
    graph[i][j] -= water
    if graph[i][j] <= 0:
        graph[i][j] = 0
        next += 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny>=m:
                continue
            if graph[nx][ny] != 0 and visited[nx][ny] == -1:
                water = 0
                for t in range(4):
                    tx = nx + dx[t]
                    ty = ny + dy[t]
                    if tx < 0 or ty < 0 or tx >=n or ty >=m:
                        continue
                    if graph[tx][ty] == 0 and visited[tx][ty] == -1:
                        water +=1
                graph[nx][ny] -= water
                if graph[nx][ny] <= 0:
                    graph[nx][ny] = 0
                    next +=1
                visited[nx][ny] = 1
                real +=1
                queue.append((nx, ny))
    return real, next

ans = 0
ans1 = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            tmp, next = bfs(i, j)
            if cnt == tmp:
                ans += 1
                cnt = cnt - next
            else:
                ans1 += 1
if not ans1:
    print(0)
else:
    print(ans)
