import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
n , m, s = map(int, input().split())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(len(graph)):
    graph[i].sort()
cnt = 1
def dfs(graph, visited, v):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph, visited, i)

dfs(graph, visited, s)

for l in range(1, len(visited)):
    print(visited[l])