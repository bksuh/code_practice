import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [0 for _ in range(n+1)]
    def dfs(start, cnt):
        visited[start] = 1
        for i in graph[start]:
            if not visited[i]:
                cnt = dfs(i, cnt+1)
        return cnt
    print(dfs(1, 0))
