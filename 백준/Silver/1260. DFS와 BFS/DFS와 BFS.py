from collections import deque
n, m ,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for elem in graph:
    elem.sort()
visited_dfs = [False]*(n+1)
def dfs(graph, visited_dfs, v):
    visited_dfs[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, visited_dfs, i)
dfs(graph, visited_dfs, v)
print()
visited_bfs = [False]*(n+1)
def bfs(graph, visited_bfs, v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)
bfs(graph, visited_bfs, v)