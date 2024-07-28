import collections
import sys

input = sys.stdin.readline

n, k, s = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for k in range(len(graph)):
    graph[k].sort(reverse=True)
def bfs(graph, visited, s):
    queue = collections.deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        current = queue.popleft()
        for k in graph[current]:
            
            if not visited[k]:
                visited[k] = visited[current] + 1
                queue.append(k)
bfs(graph, visited, s)

for i in range(1, len(visited)):
    print(visited[i]-1)