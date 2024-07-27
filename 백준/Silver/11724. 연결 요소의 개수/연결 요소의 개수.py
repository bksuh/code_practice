import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0

def bfs(graph, v, visited):
    visited[v] = True
    queue = collections.deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for k in graph[v]:
            if visited[k]:
                continue
            else:
                queue.append(k)
                visited[k] = True

if m==0:
    print(n)
else:            
    for k in range(1, len(visited)):
        if visited[k]:
            continue
        else:
            bfs(graph,k, visited)
            cnt+=1

    print(cnt)