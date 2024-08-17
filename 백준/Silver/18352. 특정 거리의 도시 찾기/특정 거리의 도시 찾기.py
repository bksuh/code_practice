import sys, heapq
INF = int(1e9)
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
heap = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        if weight > distance[now]:
            continue
        for next_node in graph[now]:
            next_weight = weight + 1
            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heapq.heappush(heap,(next_weight, next_node))

dijkstra(x)
ans = []
for i in range(1, n+1):
    if distance[i] == k:
        ans.append(i)
if ans:
    print(*ans, sep='\n')
else:
    print(-1)