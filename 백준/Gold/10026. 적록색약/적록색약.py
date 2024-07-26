import collections
n = int(input())
graph = []
graph1 = []

#Graph 두개로 분리하기
for _ in range(n):
    tmp= input()
    gr1, gr2 = [],[]
    for c in tmp:
        gr1.append(c)
        if c == 'R':
            c = 'G'
        elif c == 'B':
            c = 'X'
        gr2.append(c)
    graph.append(gr1)
    graph1.append(gr2)

dx, dy =[0,0,-1,1],[1,-1,0,0]
collor_cnt={'R':0, 'G':0, 'B':0}
def bfs(grid, colorx, x,y):
    queue = collections.deque()
    queue.append((x,y))
    grid[x][y] = 'X'
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x +dx[k]
            ny = y + dy[k]
            if nx <0 or nx>=n or ny<0 or ny >=n:
                continue
            if grid[nx][ny] == 'X' or grid[nx][ny] != colorx:
                continue
            else:
                grid[nx][ny] = 'X'
                queue.append((nx,ny))
    return grid

color1 = 'G'
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            continue
        else:
            color = graph[i][j]
            graph = bfs(graph, color,i,j)
            collor_cnt[color] +=1
cnt = 0
for i in range(n):
    for j in range(n):
        if graph1[i][j] == 'X':
            continue
        else:
            graph1 = bfs(graph1, color1,i,j)
            cnt +=1

print(collor_cnt['R'] +collor_cnt['G'] +collor_cnt['B'], cnt +collor_cnt['B'])