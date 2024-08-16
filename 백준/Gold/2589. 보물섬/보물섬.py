import collections

# 입력 받기
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    queue = collections.deque([(sx, sy)])
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    max_dist = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                max_dist = max(max_dist, dist[nx][ny])
                queue.append((nx, ny))

    return max_dist

# 모든 'L'에서 BFS 실행 후, 최대값 찾기
max_time = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            max_time = max(max_time, bfs(i, j))

print(max_time)
