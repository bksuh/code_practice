from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0,0,1,-1],[1, -1, 0, 0]

def bfs(graph, x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        c_x, c_y = queue.popleft()
        for k in range(4):
            x = c_x + dx[k]
            y = c_y + dy[k]
            if x < 0 or x >=n or y < 0 or y >=m:
                continue
            if graph[x][y] == 1:          
                queue.append((x, y))
                graph[x][y] = 0
                cnt+=1
    return cnt
res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        res.append(bfs(graph, i, j))

print(len(res))
if len(res) == 0:
    print(0)
else:
    print(max(res))