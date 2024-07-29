import collections
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
t = int(input())
for _ in range(t):
    c, r = map(int, input().split())
    graph = []
    queue = collections.deque()

    for i in range(r):
        tmp = list(input())
        for j in range(len(tmp)):
            if tmp[j] == '@':
                sx, sy = (i, j)
            elif tmp[j]=='*':
                queue.append((i, j))
        graph.append(tmp)
    graph[sx][sy] = 1
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] == '.':
                if graph[x][y] == '*':
                    graph[nx][ny] = '*'
                elif isinstance(graph[x][y], int):
                    graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            else:
                continue

    ans = 100000000
    for i in range(r):
        for j in range(c):
            
            if graph[i][j] == '#' or graph[i][j] == '*' or graph[i][j] == '.':
                continue
            elif i == 0 or i == r-1 or j == 0 or j == c-1:
                ans = min(ans, graph[i][j])

    if ans == 100000000:
        print("IMPOSSIBLE")
    else:
        print(ans)