import collections
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(n+1)

def bfs(graph, s):
    visited = [-1]*(n+1)
    visited[s] = 0
    queue = collections.deque()
    queue.append(s)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v]+1
                queue.append(i)

    return sum(visited)+1  
for i in range(1, n+1):
    ans[i] = bfs(graph, i)

real = [(k+1, v) for k, v in enumerate(ans[1::])]
real.sort(key = lambda x : (x[1], x[0]))

print(real[0][0])