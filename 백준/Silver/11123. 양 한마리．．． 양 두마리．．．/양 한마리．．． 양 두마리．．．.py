import collections

n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
def bfs(graph, x, y):
    queue = collections.deque()
    queue.append((x,y))
    graph[x][y] = '.'
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x +dx[k]
            ny = y +dy[k]
            if nx < 0 or ny < 0 or nx >= h or ny >=w:
                continue
            if graph[nx][ny] == '#':
                graph[nx][ny] = '.'
                queue.append((nx,ny))

for _ in range(n):
    h, w = map(int, input().split())
    graph = []
    for _ in range(h):
        tmp = list(input())
        graph.append(tmp)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '.':
                continue
            else:
                bfs(graph, i, j)
                cnt+=1
    print(cnt)
