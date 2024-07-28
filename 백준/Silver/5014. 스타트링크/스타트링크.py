import collections
f, s, g, u, d = map(int, input().split())

def bfs(s, g):
    visited = list(0 for _ in range(f+1))
    queue = collections.deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        v = queue.popleft()
        if v == g:
            return visited[v]-1
        for k in [v+u, v-d]:
            if k <= 0 or k > f or visited[k]:
                continue
            if visited[k] == 0:
                visited[k] = visited[v] + 1
                queue.append(k)
    return "use the stairs"
ans = bfs(s, g)
print(ans)
