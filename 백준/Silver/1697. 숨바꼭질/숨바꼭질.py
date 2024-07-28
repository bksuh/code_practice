import collections
visited = [0 for _ in range(200001)]
s, g = map(int, input().split())
def bfs(visited, s, g):
    queue = collections.deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        current = queue.popleft()
        if current == g:
            return visited[g] -1
        for k in [current-1, current+1, 2*current]:
            if k <0 or k > 200000:
                continue
            if visited[k] == 0:
                visited[k] = visited[current] + 1
                queue.append(k)
ans = bfs(visited, s, g)
print(ans)