from collections import deque
n , m = map(int, input().split())
graph = []
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for i in range(n):
    tmp = [c for c in input()]
    if 'I' in tmp:
        start = (i, tmp.index('I'))
    graph.append(tmp)

def bfs(graph, start, cnt):
    queue = deque()
    x, y = start
    queue.append(start)
    graph[x][y] = 'X'
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == 'X':
                continue
            if graph[nx][ny] == 'P':
                cnt+=1
                graph[nx][ny] = 'X'
                queue.append((nx, ny))
            else:
                graph[nx][ny] = 'X'
                queue.append((nx,ny))
    return cnt
cnt = 0
ans = bfs(graph, start, cnt)
if ans == 0:
    print('TT')
else:
    print(ans)
