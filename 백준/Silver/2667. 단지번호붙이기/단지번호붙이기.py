from collections import deque
n = int(input())
graph = [[int(c) for c in input()] for _ in range(n)]
dx, dy = [0, 0, -1, 1],[-1, 1, 0, 0]
build = []
def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >=n or ny <0 or ny >=n:
                continue
            if graph[nx][ny] == 0:
                continue
            graph[nx][ny] = 0
            cnt+=1
            queue.append((nx,ny))
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        build.append(bfs(graph, i, j))
print(len(build))
build.sort()
print(*build, sep ='\n')