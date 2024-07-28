import collections
n = int(input())
graph = [[] for _ in range(n+1)]
start, end = map(int, input().split())
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def bfs(graph, start, end):
    visited = [0 for _ in range(n+1)]
    queue = collections.deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        current = queue.popleft()
        if current == end:
            ans = visited[end] -1 
            return ans
        for i in graph[current]:
            if not visited[i]:
                visited[i] = visited[current] + 1
                queue.append(i)
    ans = -1
    return ans
ans = bfs(graph, start, end)
print(ans)
    