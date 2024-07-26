import copy
import collections

n = int(input())
ans = -1
graph = []
water_max = -1
dx, dy = [0, 0,-1,1],[1, -1, 0, 0]

def bfs(graph,water,x, y):
    queue = collections.deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue
            if graph[nx][ny] <= water or graph[nx][ny] == -1:
                continue
            else:
                graph[nx][ny] = -1
                queue.append((nx, ny))
    return graph

for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp_max = max(tmp)
    water_max = max(water_max, tmp_max)
    graph.append(tmp)

for water in range(water_max):
    tmp_graph = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] <= water or tmp_graph[i][j] == -1:
                continue
            else:
                cnt+=1
                tmp_graph = bfs(tmp_graph, water, i, j)
    ans = max(cnt, ans)
print(ans)