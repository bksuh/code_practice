import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(graph, start):
    visited = [0 for _ in range(n+1)]
    queue = collections.deque()
    queue.append(start)
    cnt = 0
    visited[start] = 1
    while queue:
        current = queue.popleft()
        for k in graph[current]:
            if not visited[k]:
                cnt += 1
                visited[k] = 1
                queue.append(k)
    return cnt


real = [0]
for p in range(1, n + 1):
    real.append(bfs(graph, p))

ans = max(real)
for i in range(1, n + 1):
    if ans == real[i]:
        print(i, end=' ')
